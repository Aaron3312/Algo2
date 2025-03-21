// Este código genera un archivo Excel para un WBS (Work Breakdown Structure)
// Para el proyecto JAI-VIER
// Puedes usar esta estructura para crear tu propio archivo Excel

const XLSX = require("xlsx");

// Crear un nuevo libro de trabajo
const workbook = XLSX.utils.book_new();

// Datos para la estructura del WBS
const wbsData = [
	[
		"ID",
		"Nivel",
		"Nombre de la Tarea",
		"Descripción",
		"Responsable",
		"Sprint",
		"Horas Estimadas",
		"Dependencias",
	],

	// Nivel 1 - Proyecto completo
	[
		"1",
		"1",
		"Proyecto JAI-VIER",
		"Herramienta de Administración de Proyectos para Oracle",
		"Todo el equipo",
		"1-15",
		"219",
		"",
	],

	// Nivel 2 - Grandes fases
	[
		"1.1",
		"2",
		"Planificación y Análisis",
		"Definición de requisitos y diseño",
		"Tellez",
		"1-2",
		"16",
		"",
	],
	[
		"1.2",
		"2",
		"Infraestructura y Configuración",
		"Configuración de entornos y base tecnológica",
		"Bañales, Aaron",
		"3",
		"75",
		"1.1",
	],
	[
		"1.3",
		"2",
		"Desarrollo Backend",
		"Implementación de microservicios y APIs",
		"Diego, Aaron",
		"4",
		"93",
		"1.2",
	],
	[
		"1.4",
		"2",
		"Desarrollo Frontend y Chatbot",
		"Implementación de interfaces y bot",
		"Aaron, Diego, Fernando",
		"5",
		"94",
		"1.3",
	],
	[
		"1.5",
		"2",
		"Integración y Pruebas",
		"Integración de componentes y pruebas",
		"Todo el equipo",
		"6",
		"83",
		"1.4",
	],
	[
		"1.6",
		"2",
		"Despliegue y Cierre",
		"Implementación final y documentación",
		"Todo el equipo",
		"7",
		"58",
		"1.5",
	],

	// Fase 1.1 - Planificación y Análisis (Sprints 1-2)
	[
		"1.1.1",
		"3",
		"Certificación OCI",
		"Capacitación en Oracle Cloud Infrastructure",
		"Todo el equipo",
		"1",
		"8",
		"",
	],
	[
		"1.1.2",
		"3",
		"Deploy 0",
		"Despliegue inicial de prueba",
		"Aaron, Bañales",
		"2",
		"8",
		"1.1.1",
	],

	// Fase 1.2 - Infraestructura y Configuración (Sprint 3)
	[
		"1.2.1",
		"3",
		"Configurar recursos básicos en OCI",
		"Configuración de VCN, compartimentos y políticas",
		"Aaron, Bañales",
		"3",
		"10",
		"1.1.2",
	],
	[
		"1.2.2",
		"3",
		"Implementar pipeline de CI/CD básico",
		"Configuración de GitHub Actions e integración",
		"Bañales",
		"3",
		"10",
		"1.2.1",
	],
	[
		"1.2.3",
		"3",
		"Implementar Oracle Autonomous Database",
		"Configuración de base de datos y esquemas",
		"Diego, Tellez",
		"3",
		"8",
		"1.2.1",
	],
	[
		"1.2.4",
		"3",
		"Configurar entornos Kubernetes",
		"Provisionar OKE y configurar recursos",
		"Bañales",
		"3",
		"12",
		"1.2.1",
	],
	[
		"1.2.5",
		"3",
		"Configurar entornos de desarrollo",
		"Scripts de aprovisionamiento y documentación",
		"Tellez",
		"3",
		"6",
		"1.2.2",
	],
	[
		"1.2.6",
		"3",
		"Crear estructura base de microservicios",
		"Implementación de proyectos base con Spring Boot",
		"Diego, Aaron",
		"3",
		"15",
		"1.2.3",
	],
	[
		"1.2.7",
		"3",
		"Configurar API Gateway",
		"Implementación y configuración de gateway",
		"Diego",
		"3",
		"8",
		"1.2.4",
	],
	[
		"1.2.8",
		"3",
		"Preparar integración con Telegram",
		"Investigación de API y bot básico de prueba",
		"Fernando, Aram",
		"3",
		"6",
		"1.2.6",
	],

	// Fase 1.3 - Desarrollo Backend (Sprint 4)
	[
		"1.3.1",
		"3",
		"Implementar microservicio de Gestión de Usuarios",
		"APIs CRUD y lógica de autenticación",
		"Diego",
		"4",
		"12",
		"1.2.6",
	],
	[
		"1.3.2",
		"3",
		"Implementar microservicio de Gestión de Proyectos",
		"APIs CRUD y lógica de proyectos",
		"Aaron",
		"4",
		"14",
		"1.2.6",
	],
	[
		"1.3.3",
		"3",
		"Implementar microservicio de Gestión de Tareas",
		"APIs CRUD y lógica de workflow",
		"Diego, Aaron",
		"4",
		"15",
		"1.3.1, 1.3.2",
	],
	[
		"1.3.4",
		"3",
		"Implementar microservicio de Análisis y KPIs",
		"Algoritmos para cálculo de métricas",
		"Bañales",
		"4",
		"16",
		"1.3.3",
	],
	[
		"1.3.5",
		"3",
		"Implementar pruebas unitarias para microservicios",
		"Desarrollo de tests y cobertura",
		"Fernando",
		"4",
		"10",
		"1.3.1, 1.3.2, 1.3.3, 1.3.4",
	],
	[
		"1.3.6",
		"3",
		"Implementar pruebas de integración",
		"Tests end-to-end y validación de flujos",
		"Fernando, Aram",
		"4",
		"8",
		"1.3.5",
	],
	[
		"1.3.7",
		"3",
		"Integrar todos los microservicios",
		"Comunicación entre servicios y resolución de dependencias",
		"Aaron, Diego",
		"4",
		"10",
		"1.3.5",
	],
	[
		"1.3.8",
		"3",
		"Implementar seguridad en APIs",
		"JWT/OAuth2 y control de acceso",
		"Tellez",
		"4",
		"8",
		"1.3.7",
	],

	// Fase 1.4 - Desarrollo Frontend y Chatbot (Sprint 5)
	[
		"1.4.1",
		"3",
		"Configurar proyecto frontend",
		"Setup de React y estructura base",
		"Aaron",
		"5",
		"8",
		"1.3.8",
	],
	[
		"1.4.2",
		"3",
		"Desarrollar módulo de autenticación",
		"Pantallas de login y manejo de tokens",
		"Aaron, Aram",
		"5",
		"10",
		"1.4.1",
	],
	[
		"1.4.3",
		"3",
		"Desarrollar dashboard principal",
		"Widgets para KPIs y visualizaciones",
		"Aaron",
		"5",
		"12",
		"1.4.2",
	],
	[
		"1.4.4",
		"3",
		"Desarrollar módulo de gestión de proyectos",
		"CRUD y vistas de proyectos",
		"Aaron, Aram",
		"5",
		"14",
		"1.4.3",
	],
	[
		"1.4.5",
		"3",
		"Desarrollar módulo de gestión de tareas",
		"Vista Kanban y seguimiento de tiempo",
		"Aaron, Aram",
		"5",
		"14",
		"1.4.4",
	],
	[
		"1.4.6",
		"3",
		"Desarrollar estructura base del chatbot",
		"Integración con Telegram y comandos básicos",
		"Diego, Fernando",
		"5",
		"10",
		"1.2.8",
	],
	[
		"1.4.7",
		"3",
		"Implementar comandos para gestión de proyectos",
		"Comandos para gestionar proyectos vía bot",
		"Diego",
		"5",
		"8",
		"1.4.6",
	],
	[
		"1.4.8",
		"3",
		"Implementar comandos para gestión de tareas",
		"Comandos para gestionar tareas vía bot",
		"Diego, Bañales",
		"5",
		"10",
		"1.4.7",
	],
	[
		"1.4.9",
		"3",
		"Implementar consultas de KPIs vía bot",
		"Comandos para consultar métricas",
		"Bañales",
		"5",
		"8",
		"1.4.8",
	],

	// Fase 1.5 - Integración y Pruebas (Sprint 6)
	[
		"1.5.1",
		"3",
		"Integrar frontend con backend",
		"Resolver problemas de integración API",
		"Aaron, Diego",
		"6",
		"12",
		"1.4.5, 1.3.8",
	],
	[
		"1.5.2",
		"3",
		"Integrar chatbot con backend",
		"Finalizar integración de comandos",
		"Diego, Bañales",
		"6",
		"10",
		"1.4.9, 1.3.8",
	],
	[
		"1.5.3",
		"3",
		"Implementar sistema de notificaciones cruzadas",
		"Notificaciones web y Telegram",
		"Bañales, Tellez",
		"6",
		"8",
		"1.5.1, 1.5.2",
	],
	[
		"1.5.4",
		"3",
		"Realizar pruebas de rendimiento",
		"Identificar y resolver cuellos de botella",
		"Fernando, Aram",
		"6",
		"10",
		"1.5.3",
	],
	[
		"1.5.5",
		"3",
		"Realizar pruebas de seguridad",
		"Análisis de vulnerabilidades",
		"Tellez",
		"6",
		"8",
		"1.5.3",
	],
	[
		"1.5.6",
		"3",
		"Realizar pruebas de usabilidad",
		"Sesiones con usuarios y feedback",
		"Fernando, Aram",
		"6",
		"10",
		"1.5.1",
	],
	[
		"1.5.7",
		"3",
		"Corrección de bugs identificados",
		"Priorización y resolución de errores",
		"Todo el equipo",
		"6",
		"15",
		"1.5.4, 1.5.5, 1.5.6",
	],
	[
		"1.5.8",
		"3",
		"Finalizar documentación técnica",
		"Completar docs de APIs y arquitectura",
		"Tellez, Diego",
		"6",
		"10",
		"1.5.7",
	],

	// Fase 1.6 - Despliegue y Cierre (Sprint 7)
	[
		"1.6.1",
		"3",
		"Preparar entorno de producción",
		"Configuración final de infraestructura",
		"Bañales, Tellez",
		"7",
		"10",
		"1.5.8",
	],
	[
		"1.6.2",
		"3",
		"Despliegue de todos los componentes",
		"Implementación en producción",
		"Bañales, Aaron",
		"7",
		"12",
		"1.6.1",
	],
	[
		"1.6.3",
		"3",
		"Pruebas post-despliegue",
		"Verificación en producción",
		"Fernando, Aram",
		"7",
		"8",
		"1.6.2",
	],
	[
		"1.6.4",
		"3",
		"Finalizar documentación de usuario",
		"Manuales y guías de referencia",
		"Tellez, Fernando",
		"7",
		"10",
		"1.6.3",
	],
	[
		"1.6.5",
		"3",
		"Preparar presentación final",
		"Diapositivas y demo",
		"Todo el equipo",
		"7",
		"8",
		"1.6.4",
	],
	[
		"1.6.6",
		"3",
		"Sesión de lecciones aprendidas",
		"Retrospectiva del proyecto",
		"Todo el equipo",
		"7",
		"4",
		"1.6.5",
	],
	[
		"1.6.7",
		"3",
		"Entrega formal del proyecto",
		"Entrega de accesos y entrenamiento",
		"Tellez, Aaron",
		"7",
		"6",
		"1.6.6",
	],
];

// Crear hoja de trabajo para el WBS
const ws = XLSX.utils.aoa_to_sheet(wbsData);

// Establecer ancho de columnas
const colWidths = [10, 10, 45, 60, 25, 15, 15, 20];
ws["!cols"] = colWidths.map((w) => ({ width: w }));

// Añadir la hoja de trabajo al libro
XLSX.utils.book_append_sheet(workbook, ws, "WBS JAI-VIER");

// Crear hoja secundaria para diagrama Gantt
const ganttData = [
	[
		"ID",
		"Tarea",
		"Responsable",
		"Fecha Inicio",
		"Duración (días)",
		"Dependencias",
	],
	// Aquí puedes añadir los datos para un diagrama Gantt si lo necesitas
];

const wsGantt = XLSX.utils.aoa_to_sheet(ganttData);
XLSX.utils.book_append_sheet(workbook, wsGantt, "Diagrama Gantt");

// Crear hoja para Matriz RACI
const raciData = [
	[
		"Tarea/Actividad",
		"Tellez (PM)",
		"Bañales (DevOps)",
		"Diego (Back)",
		"Aaron (Full)",
		"Fernando (QA)",
		"Aram (Intern)",
	],
	["Planificación", "R", "C", "C", "C", "I", "I"],
	["Infraestructura OCI", "A", "R", "C", "C", "I", "I"],
	["Base de Datos", "C", "C", "R", "I", "I", "I"],
	["Microservicios", "A", "C", "R", "R", "C", "I"],
	["Frontend", "A", "I", "C", "R", "C", "C"],
	["Bot Telegram", "A", "C", "R", "I", "C", "C"],
	["Testing", "A", "I", "C", "C", "R", "C"],
	["Despliegue", "A", "R", "C", "C", "I", "I"],
	["Documentación", "R", "C", "C", "C", "C", "I"],
	// R: Responsible, A: Accountable, C: Consulted, I: Informed
];

const wsRaci = XLSX.utils.aoa_to_sheet(raciData);
XLSX.utils.book_append_sheet(workbook, wsRaci, "Matriz RACI");

// Crear una hoja para el glosario y leyendas
const glossaryData = [
	["Término", "Descripción"],
	["WBS", "Work Breakdown Structure - Estructura de desglose del trabajo"],
	["OCI", "Oracle Cloud Infrastructure"],
	["CI/CD", "Continuous Integration/Continuous Deployment"],
	["API", "Application Programming Interface"],
	[
		"CRUD",
		"Create, Read, Update, Delete - Operaciones básicas de base de datos",
	],
	["JWT", "JSON Web Token - Método de autenticación"],
	["KPI", "Key Performance Indicator - Indicador clave de rendimiento"],
	["Matriz RACI", "R: Responsible, A: Accountable, C: Consulted, I: Informed"],
	["Sprint", "Período definido de tiempo para completar un conjunto de tareas"],
	["Nivel en WBS", "1: Proyecto, 2: Fase, 3: Actividad, 4: Tarea"],
];

const wsGlossary = XLSX.utils.aoa_to_sheet(glossaryData);
XLSX.utils.book_append_sheet(workbook, wsGlossary, "Glosario");

// Si estuvieras ejecutando este código en Node.js, guardarías el archivo así:
XLSX.writeFile(workbook, "JAI-VIER_WBS.xlsx");

// Estructura de las hojas generadas:
console.log("Estructura del libro Excel generado:");
console.log("- Hoja 1: WBS JAI-VIER - Estructura de desglose completa");
console.log(
	"- Hoja 2: Diagrama Gantt - Base para crear un diagrama de programación"
);
console.log("- Hoja 3: Matriz RACI - Asignación de responsabilidades");
console.log("- Hoja 4: Glosario - Términos y definiciones");
