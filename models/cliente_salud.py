from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import re

class ClienteSalud(models.Model):
    _name = 'cliente.salud'
    _description = 'Información de Salud del Cliente'

    # Campos de identificación
    nombre = fields.Char(string='Nombre', required=True)
    apellidos = fields.Char(string='Apellidos', required=True)
    dni = fields.Char(string='DNI', required=True, unique=True)
    edad = fields.Integer(string='Edad', required=True)

    # Datos físicos
    altura = fields.Float(string='Altura (m)', required=True)
    peso = fields.Float(string='Peso (kg)', required=True)
    imc = fields.Float(string='IMC', compute='_compute_imc', store=True)
    imc_category = fields.Selection([
        ('bajo_peso', 'Bajo Peso'),
        ('normal', 'Peso Normal'),
        ('sobrepeso', 'Sobrepeso'),
        ('obesidad1', 'Obesidad Tipo 1'),
        ('obesidad2', 'Obesidad Tipo 2'),
        ('obesidad3', 'Obesidad Tipo 3'),
    ], string='Clasificación IMC', compute='_compute_imc_category', store=True)

    # Metas y progresos
    kcal_goal = fields.Float(string='Objetivo de KCAL/semana', required=True)
    recommended_activity = fields.Text(string='Actividad Recomendada', compute='_compute_recommended_activity')
    diet_recommendation = fields.Text(string='Recomendación de Dieta', compute='_compute_diet_recommendation')
    progress_notes = fields.Text(string='Notas de Progreso')

    # Historial de actividades
    activity_history = fields.One2many('cliente.salud.activity', 'cliente_id', string='Historial de Actividades')

    # Validación del DNI
    @api.constrains('dni')
    def _check_dni(self):
        for record in self:
            if not re.match(r'^\d{8}[A-Z]$', record.dni):
                raise ValidationError(_("El DNI debe tener 8 números seguidos de una letra mayúscula."))

    # Validación de la edad
    @api.constrains('edad')
    def _check_edad(self):
        for record in self:
            if not (0 <= record.edad <= 120):
                raise ValidationError(_("La edad debe estar entre 0 y 120 años."))

    # Cálculo del IMC
    @api.depends('peso', 'altura')
    def _compute_imc(self):
        for record in self:
            if record.altura > 0:
                record.imc = round(record.peso / (record.altura ** 2), 2)
            else:
                record.imc = 0.0

    # Clasificación del IMC
    @api.depends('imc')
    def _compute_imc_category(self):
        for record in self:
            if record.imc < 18.5:
                record.imc_category = 'bajo_peso'
            elif 18.5 <= record.imc < 24.9:
                record.imc_category = 'normal'
            elif 25 <= record.imc < 29.9:
                record.imc_category = 'sobrepeso'
            elif 30 <= record.imc < 34.9:
                record.imc_category = 'obesidad1'
            elif 35 <= record.imc < 39.9:
                record.imc_category = 'obesidad2'
            else:
                record.imc_category = 'obesidad3'

    # Cálculo de actividad recomendada
    @api.depends('imc_category')
    def _compute_recommended_activity(self):
        for record in self:
            if record.imc_category in ['obesidad1', 'obesidad2', 'obesidad3']:
                record.recommended_activity = _('Ejercicio de bajo impacto: caminar, nadar, yoga.')
            elif record.imc_category == 'sobrepeso':
                record.recommended_activity = _('Ejercicio moderado: bicicleta, entrenamiento de fuerza ligero.')
            else:
                record.recommended_activity = _('Ejercicio intenso: correr, HIIT, entrenamiento con pesas.')

    # Cálculo de la recomendación de dieta
    @api.depends('kcal_goal')
    def _compute_diet_recommendation(self):
        for record in self:
            if record.kcal_goal > 2500:
                record.diet_recommendation = _('Dieta hipocalórica con alto contenido en proteínas y fibra.')
            elif 1500 <= record.kcal_goal <= 2500:
                record.diet_recommendation = _('Dieta balanceada con moderación en carbohidratos y grasas.')
            else:
                record.diet_recommendation = _('Dieta de mantenimiento con un buen equilibrio de macronutrientes.')

class ClienteSaludActivity(models.Model):
    _name = 'cliente.salud.activity'
    _description = 'Historial de Actividades del Cliente'

    cliente_id = fields.Many2one('cliente.salud', string='Cliente', required=True, ondelete='cascade')
    activity_date = fields.Date(string='Fecha de Actividad', required=True)
    activity_type = fields.Selection([
        ('correr', 'Correr'),
        ('caminar', 'Caminar'),
        ('nadar', 'Nadar'),
        ('ciclismo', 'Ciclismo'),
        ('gimnasio', 'Gimnasio'),
        ('yoga', 'Yoga'),
        ('otro', 'Otro'),
    ], string='Tipo de Actividad', required=True)
    duration = fields.Float(string='Duración (minutos)', required=True)
    notes = fields.Text(string='Notas')
