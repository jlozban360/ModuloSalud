# Módulo Personalizado de Odoo: Cliente Salud

## Descripción
Este módulo personalizado para Odoo permite la gestión de la información de salud de los clientes. Incluye funcionalidades para registrar datos personales, calcular el IMC, establecer objetivos calóricos semanales y sugerir actividades físicas y recomendaciones dietéticas en base a la información proporcionada.

## Características Principales
- Registro de clientes con datos personales y de salud.
- Cálculo automático del IMC (Índice de Masa Corporal).
- Validaciones para edad, altura y formato de DNI.
- Sugerencias de actividad física según el IMC.
- Recomendaciones de dieta en función del objetivo calórico semanal.
- Historial de actividades realizadas por el cliente.

## Instalación
1. Clona este repositorio en el directorio de módulos personalizados de tu instancia de Odoo:
   ```bash
   git clone https://github.com/tuusuario/odoo-cliente-salud.git
   ```
2. Reinicia el servidor de Odoo:
   ```bash
   odoo-bin -c /ruta/a/tu/configuracion.conf -u cliente_salud
   ```
3. Accede a Odoo y activa el módulo desde la interfaz de aplicaciones.

## Uso
1. Navega a la sección **Clientes de Salud** en Odoo.
2. Agrega un nuevo cliente proporcionando sus datos personales.
3. Introduce información sobre peso, altura y objetivos calóricos.
4. Visualiza recomendaciones automáticas de actividad y dieta.
5. Registra el historial de actividades para el seguimiento del progreso.

## Dependencias
Este módulo requiere:
- Odoo 14 o superior.
- Python 3.6+
- Dependencias de Odoo relacionadas con modelos, campos y restricciones.
