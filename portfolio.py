import json

import streamlit as st
import streamlit.components.v1 as components

# ─────────────────────────────────────────────
# CONFIGURAÇÃO DA PÁGINA
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Renan Britto · Portfólio de Dados",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────
# DADOS FIXOS
# ─────────────────────────────────────────────
PROFILE = {
    "name": "Renan Britto",
    "linkedin": "https://linkedin.com/in/renan-britto-7b3728212/",
    "github": "https://github.com/Renanbritto",
    "email": "mailto:renanbritto.py@gmail.com",
}

LANG_OPTIONS = {
    "pt": {"flag": "🇧🇷", "label": "Português (BR)"},
    "en": {"flag": "🇺🇸", "label": "English"},
}

NAV_ITEMS = {
    "home": {"pt": "🏠  Home", "en": "🏠  Home"},
    "about": {"pt": "👤  Sobre mim", "en": "👤  About Me"},
    "skills": {"pt": "⚙️  Skills", "en": "⚙️  Skills"},
    "projects": {"pt": "📁  Projetos", "en": "📁  Projects"},
    "method": {"pt": "🔍  Meu método", "en": "🔍  My Method"},
    "experience": {"pt": "💼  Experiência", "en": "💼  Experience"},
    "contact": {"pt": "✉️  Contato", "en": "✉️  Contact"},
}

SECTION_ORDER = list(NAV_ITEMS.keys())

CONTENT = {
    "pt": {
        "location": "Brasil",
        "headline": "Dados, Automação & BI",
        "hero_title": "Construindo soluções com dados, automação e visão de negócio.",
        "hero_summary": (
            "Sou estudante de Ciência da Computação e estudo dados há bastante tempo, "
            "desenvolvendo base em análise, visualização, automação e resolução de problemas "
            "orientados por dados. Ao longo da minha trajetória, já utilizei dados em diferentes "
            "contextos profissionais, mesmo antes de atuar formalmente em uma função exclusiva da área. "
            "Desde fevereiro de 2026, atuo em um cargo dedicado a dados como Estagiário em Automação "
            "e Business Intelligence, unindo aprendizado contínuo, prática técnica e foco em gerar valor."
        ),
        "hero_panel": {
            "label": "Camada de foco",
            "value": "Data + Automation",
            "text": "Soluções com visão de negócio, leitura analítica e construção prática.",
            "cards": [
                ("Python", "automation"),
                ("SQL", "querying"),
                ("BI", "dashboards"),
                ("Data", "analytics"),
            ],
        },
        "stack_items": [
            "Python",
            "SQL",
            "Power BI",
            "Streamlit",
            "Pandas",
            "Automação",
            "Analytics",
            "Business Intelligence",
        ],
        "metrics": [
            ("Fev/2026", "Atuação profissional dedicada em dados"),
            ("Python + SQL", "Base técnica principal"),
            ("BI + Automação", "Foco atual"),
            ("Acadêmico + Profissional", "Experiência aplicada"),
        ],
        "sidebar_note": "Aberto para oportunidades em dados, automação e BI.",
        "buttons": {
            "linkedin": "LinkedIn",
            "github": "GitHub",
            "email": "Enviar e-mail",
            "project": "Ver projeto →",
            "contact": "Enviar mensagem",
        },
        "about": {
            "eyebrow": "Perfil",
            "title": "Sobre mim",
            "subtitle": "Estudante de Ciência da Computação com trajetória prática em dados, automação, análise e BI.",
            "paragraphs": [
                (
                    "Sou estudante de Ciência da Computação com foco em Dados, Analytics, Automação e Business Intelligence. "
                    "Minha trajetória com dados começou antes de ocupar formalmente uma função dedicada à área, por meio de estudos, "
                    "projetos e aplicações práticas em empresas pelas quais passei."
                ),
                (
                    "Mesmo em experiências anteriores que não tinham o título oficialmente voltado a dados, já atuava com análise de informações, "
                    "estruturação de controles, relatórios, apoio à tomada de decisão e melhoria de processos com base em dados."
                ),
                (
                    "Desde fevereiro de 2026, passei a atuar diretamente em um cargo dedicado à área como Estagiário em Automação e Business Intelligence. "
                    "Hoje, meu foco está em transformar dados em informação útil, automatizar rotinas e construir soluções analíticas que apoiem o negócio de forma prática."
                ),
            ],
            "areas": [
                {
                    "icon": "🎓",
                    "title": "Base em Ciência da Computação",
                    "desc": "Formação que fortalece lógica, programação, estruturação de problemas e visão técnica.",
                },
                {
                    "icon": "📊",
                    "title": "Business Intelligence",
                    "desc": "Construção de dashboards, indicadores e relatórios para acompanhamento de resultados.",
                },
                {
                    "icon": "🔄",
                    "title": "Automação",
                    "desc": "Uso de Python, SQL e ferramentas analíticas para reduzir esforço manual e ganhar eficiência.",
                },
                {
                    "icon": "📈",
                    "title": "Evolução em Dados",
                    "desc": "Trajetória construída com estudo contínuo, prática aplicada e aprofundamento técnico constante.",
                },
            ],
        },
        "skills": {
            "eyebrow": "Stack",
            "title": "Skills e Ferramentas",
            "subtitle": "",
            "note": "",
            "groups": [
                {
                    "title": "Análise de Dados",
                    "icon": "◔",
                    "tools": [
                        "Pandas",
                        "NumPy",
                        "EDA",
                        "Data Cleaning",
                        "Storytelling com Dados",
                        "Análise Exploratória",
                    ],
                },
                {
                    "title": "BI e Visualização",
                    "icon": "▣",
                    "tools": [
                        "Power BI",
                        "DAX",
                        "Modelagem de Dados",
                        "Streamlit",
                        "Matplotlib",
                        "Seaborn",
                        "Plotly",
                    ],
                },
                {
                    "title": "Ciência de Dados",
                    "icon": "◎",
                    "tools": [
                        "Scikit-learn",
                        "Classificação",
                        "Regressão",
                        "Clustering",
                        "Feature Engineering",
                        "Model Evaluation",
                    ],
                },
                {
                    "title": "Estatística Aplicada",
                    "icon": "≈",
                    "tools": [
                        "Estatística Descritiva",
                        "Correlação",
                        "Distribuições",
                        "Testes de Hipótese",
                        "Métricas de Performance",
                        "A/B Testing",
                    ],
                },
                {
                    "title": "Dados e Bancos",
                    "icon": "▤",
                    "tools": [
                        "SQL Server",
                        "MySQL",
                        "PostgreSQL",
                        "T-SQL",
                        "ETL",
                        "Data Quality",
                        "Data Warehousing",
                    ],
                },
                {
                    "title": "Programação e Automação",
                    "icon": "↻",
                    "tools": [
                        "Python",
                        "Jupyter Notebook",
                        "Git / GitHub",
                        "APIs",
                        "VBA",
                        "Scripting",
                    ],
                },
            ],
        },
        "projects": {
            "eyebrow": "Projetos",
            "title": "Projetos e estudos aplicados",
            "subtitle": "Exemplos de aplicação prática em dashboards, automação, qualidade de dados e estudos analíticos.",
            "problem": "Problema",
            "insights": "Insights",
            "impact": "Impacto",
            "items": [
                {
                    "title": "Dashboard de Indicadores de Negócio",
                    "emoji": "📊",
                    "problem": "A área precisava acompanhar indicadores com mais clareza e menos dependência de controles manuais.",
                    "insights": "A estruturação dos dados e dos KPIs tornou a análise mais rápida, padronizada e visualmente mais clara.",
                    "impact": "A solução melhorou a leitura dos resultados e apoiou o acompanhamento mais consistente das métricas.",
                    "tools": ["Power BI", "SQL", "DAX", "Excel"],
                    "link": "#",
                },
                {
                    "title": "Automação de Rotinas com Python",
                    "emoji": "🔄",
                    "problem": "Parte do trabalho operacional dependia de tarefas repetitivas, com tempo alto de execução manual.",
                    "insights": "Ao mapear as etapas do processo, foi possível identificar pontos de padronização, validação e automação.",
                    "impact": "A automação reduziu retrabalho, aumentou produtividade e melhorou a confiabilidade das entregas.",
                    "tools": ["Python", "Pandas", "Excel", "Automação"],
                    "link": "#",
                },
                {
                    "title": "Estudo de Qualidade de Dados",
                    "emoji": "🔍",
                    "problem": "Bases com inconsistências e campos incompletos prejudicavam relatórios e interpretações posteriores.",
                    "insights": "A análise evidenciou padrões de preenchimento incorreto, dados faltantes e registros com baixa confiabilidade.",
                    "impact": "O estudo contribuiu para maior confiança nas informações e para a criação de critérios de validação.",
                    "tools": ["Python", "Pandas", "SQL", "Data Quality"],
                    "link": "#",
                },
                {
                    "title": "Estudo Aplicado de Previsão",
                    "emoji": "📈",
                    "problem": "Em alguns contextos, antecipar comportamento de demanda ou tendência pode apoiar o planejamento.",
                    "insights": "A análise temporal e o uso de modelos simples mostraram o potencial de previsões como apoio à tomada de decisão.",
                    "impact": "O projeto reforçou minha base em Ciência de Dados e mostrou como modelos podem complementar a análise descritiva.",
                    "tools": ["Python", "Scikit-learn", "Time Series", "Pandas"],
                    "link": "#",
                },
            ],
        },
        "method": {
            "eyebrow": "Método",
            "title": "Meu método analítico",
            "subtitle": "",
            "note": "",
            "principles_title": "Princípios que guiam meu trabalho",
            "steps": [
                ("🎯", "Problema", "Entender a necessidade, o contexto do negócio e o objetivo da análise."),
                ("🗂️", "Dados", "Mapear fontes, estrutura, qualidade e disponibilidade das informações."),
                ("🧪", "Hipóteses", "Definir perguntas, métricas e abordagem analítica para investigar o problema."),
                ("🔧", "Tratamento", "Limpar, transformar e organizar os dados para análise ou modelagem."),
                ("📊", "Análise", "Explorar padrões, testar hipóteses e construir visualizações ou modelos."),
                ("✅", "Entrega", "Traduzir os resultados em insight, dashboard, automação ou recomendação prática."),
            ],
            "principles": [
                ("Negócio antes da ferramenta", "A tecnologia deve servir ao problema real, não o contrário."),
                ("Dados confiáveis primeiro", "Antes de analisar ou modelar, é preciso garantir consistência e entendimento da base."),
                ("Clareza na comunicação", "Uma análise só gera valor quando pode ser entendida e utilizada por quem decide."),
                ("Automatizar o que faz sentido", "Ganhos de produtividade aparecem quando tarefas recorrentes são bem estruturadas e automatizadas."),
                ("Aprendizado contínuo", "Minha evolução em dados é construída com estudo, prática e aprofundamento constante."),
                ("Solução aplicável", "O objetivo final é sempre gerar algo utilizável: insight, processo, painel ou melhoria prática."),
            ],
        },
        "experience": {
            "eyebrow": "Experiência",
            "title": "Trajetória profissional",
            "subtitle": "Uma evolução construída com estudo, prática aplicada e atuação direta em Automação e Business Intelligence.",
            "items": [
                {
                    "role": "Automação e Business Intelligence",
                    "company": "Nossa Loja",
                    "period": "02/2026 – Atual",
                    "bullets": [
                        "Atuação dedicada à área de dados, com foco em automação de processos e Business Intelligence.",
                        "Apoio na construção e manutenção de relatórios, dashboards e indicadores para acompanhamento de resultados.",
                        "Uso de ferramentas e rotinas analíticas para organizar dados, melhorar fluxos e apoiar decisões.",
                        "Desenvolvimento contínuo de habilidades em análise de dados, visualização, automação e estruturação de informações.",
                    ],
                },
                {
                    "role": "Analista de Suporte",
                    "company": "FDC Sistemas",
                    "period": "02/2025 - 09/2025",
                    "bullets": [
                        "Suporte a sistemas ERP: Atendimento a usuários do ERP FDC Sistemas, atuando na resolução de incidentes e no suporte operacional, garantindo o uso eficiente da plataforma.",
                        "Relatórios Completos:criação de relatórios utilizando SQL, garantindo o uso eficiente da plataforma e a disponibilização de informações para tomada de decisão.",
                    ],
                },
                {
                    "role": "Técnico de Infraestrutura",
                    "company": "Netsupport",
                    "period": "10/2024 - 12/2024",
                    "bullets": [
                        "Implantação e configuração de redes: Planejamento e implementação de redes LAN e Wi-Fi, garantindo conectividade estável em ambientes educacionais (salas, laboratórios e áreas administrativas).",
                        "Modelagem de infraestrutura de rede: Elaboração de layouts e diagramas de topologia, documentando a arquitetura de redes (roteadores, switches, access points e cabeamento).",
                        "Contato com melhoria de processos, acompanhamento de indicadores e uso prático de dados no contexto do negócio.",
                        "Criação e atualização de documentação de infraestrutura, registros de manutenção e relatórios operacionais.",
                    ],
                },
                {
                    "role": "Sales Development Representative",
                    "company": "Projetil",
                    "period": "04/2024 - 10/2024",
                    "bullets": [
                        "Entendimento de requisitos do cliente: Atuação direta com clientes oriundos da área comercial, identificando necessidades, dores e oportunidades para definição de soluções tecnológicas aderentes ao negócio.",
                        "Negociação e fechamento de projetos: Condução de negociações técnicas e comerciais, garantindo clareza na proposta de valor e efetivação de contratos.",
                        "Planejamento de projetos: Estruturação do escopo completo dos projetos, com definição de etapas, entregas e alinhamento prévio com áreas envolvidas.",
                        "Gestão técnica de soluções: Aplicação de conhecimentos em programação para suporte técnico, validação de soluções e garantia de escalabilidade e robustez.",
                    ],
                },
             
            ],
        },
        "contact": {
            "eyebrow": "Contato",
            "title": "Vamos conversar",
            "subtitle": "Disponível para oportunidades de aprendizado, estágio, projetos e conexões na área de dados.",
            "intro_1": (
                "Estou em desenvolvimento constante na área de Dados, com foco em Automação, BI e análise. "
                "Tenho interesse em oportunidades que me permitam evoluir tecnicamente e gerar impacto real com dados."
            ),
            "intro_2": (
                "Se você procura alguém com base técnica, vontade de aprender, visão analítica e dedicação, "
                "será um prazer conversar."
            ),
            "cta_title": "Vamos conversar sobre dados?",
            "cta_text": "Estou aberto a conexões, oportunidades e projetos em Automação, BI e Análise de Dados.",
            "items": [
                ("✉️", "Email", "renanbritto.py@gmail.com", "mailto:renanbritto.py@gmail.com"),
                ("💼", "LinkedIn", "linkedin.com/in/renan-britto-7b3728212/", "https://www.linkedin.com/in/renan-britto-7b3728212/"),
                ("🐙", "GitHub", "github.com/Renanbritto", "https://github.com/Renanbritto"),
            ],
        },
        "footer": "Renan Britto · Portfólio de Dados · 2026",
    },
    "en": {
        "location": "Brazil",
        "headline": "Data, Automation & BI",
        "hero_title": "Building solutions with data, automation and business vision.",
        "hero_summary": (
            "I am a Computer Science student and I have been studying data for a long time, "
            "building a strong foundation in analysis, visualization, automation and data-driven problem solving. "
            "Throughout my journey, I have already applied data in different professional contexts, even before working "
            "in a role exclusively dedicated to the area. Since February 2026, I have been working in a dedicated data role "
            "as an Automation and Business Intelligence Intern, combining continuous learning, technical practice and business impact."
        ),
        "hero_panel": {
            "label": "Focus Layer",
            "value": "Data + Automation",
            "text": "Solutions with business vision, analytical thinking and practical execution.",
            "cards": [
                ("Python", "automation"),
                ("SQL", "querying"),
                ("BI", "dashboards"),
                ("Data", "analytics"),
            ],
        },
        "stack_items": [
            "Python",
            "SQL",
            "Power BI",
            "Streamlit",
            "Pandas",
            "Automation",
            "Analytics",
            "Business Intelligence",
        ],
        "metrics": [
            ("Feb/2026", "Dedicated professional role in data"),
            ("Python + SQL", "Main technical foundation"),
            ("BI + Automation", "Current focus"),
            ("Academic + Professional", "Applied experience"),
        ],
        "sidebar_note": "Open to opportunities in data, automation and BI.",
        "buttons": {
            "linkedin": "LinkedIn",
            "github": "GitHub",
            "email": "Send email",
            "project": "View project →",
            "contact": "Send message",
        },
        "about": {
            "eyebrow": "Profile",
            "title": "About me",
            "subtitle": "Computer Science student with practical experience in data, automation, analytics and BI.",
            "paragraphs": [
                (
                    "I am a Computer Science student focused on Data, Analytics, Automation and Business Intelligence. "
                    "My journey with data started before I formally held a dedicated role in the field, through study, projects "
                    "and practical applications in the companies I worked for."
                ),
                (
                    "Even in previous roles that were not officially labeled as data positions, I already worked with information analysis, "
                    "control structuring, reporting, decision support and process improvement based on data."
                ),
                (
                    "Since February 2026, I have been working directly in a dedicated role in the area as an Automation and Business Intelligence Intern. "
                    "Today, my focus is on transforming data into useful information, automating routines and building analytical solutions that practically support the business."
                ),
            ],
            "areas": [
                {
                    "icon": "🎓",
                    "title": "Computer Science Foundation",
                    "desc": "Education that strengthens logic, programming, problem structuring and technical vision.",
                },
                {
                    "icon": "📊",
                    "title": "Business Intelligence",
                    "desc": "Dashboards, indicators and reporting solutions to track business performance.",
                },
                {
                    "icon": "🔄",
                    "title": "Automation",
                    "desc": "Using Python, SQL and analytical tools to reduce manual work and improve efficiency.",
                },
                {
                    "icon": "📈",
                    "title": "Growth in Data",
                    "desc": "A path built through continuous study, practical application and constant technical improvement.",
                },
            ],
        },
        "skills": {
            "eyebrow": "Stack",
            "title": "Skills & Tools",
            "subtitle": "My skills organized in a vertical visual flow, connecting analysis, visualization, statistics, data and automation.",
            "note": "Hover over the blocks to explore each area.",
            "groups": [
                {
                    "title": "Data Analysis",
                    "icon": "◔",
                    "tools": [
                        "Pandas",
                        "NumPy",
                        "EDA",
                        "Data Cleaning",
                        "Data Storytelling",
                        "Exploratory Analysis",
                    ],
                },
                {
                    "title": "BI & Visualization",
                    "icon": "▣",
                    "tools": [
                        "Power BI",
                        "DAX",
                        "Data Modeling",
                        "Streamlit",
                        "Matplotlib",
                        "Seaborn",
                        "Plotly",
                    ],
                },
                {
                    "title": "Data Science",
                    "icon": "◎",
                    "tools": [
                        "Scikit-learn",
                        "Classification",
                        "Regression",
                        "Clustering",
                        "Feature Engineering",
                        "Model Evaluation",
                    ],
                },
                {
                    "title": "Applied Statistics",
                    "icon": "≈",
                    "tools": [
                        "Descriptive Statistics",
                        "Correlation",
                        "Distributions",
                        "Hypothesis Testing",
                        "Performance Metrics",
                        "A/B Testing",
                    ],
                },
                {
                    "title": "Data & Databases",
                    "icon": "▤",
                    "tools": [
                        "SQL Server",
                        "MySQL",
                        "PostgreSQL",
                        "T-SQL",
                        "ETL",
                        "Data Quality",
                        "Data Warehousing",
                    ],
                },
                {
                    "title": "Programming & Automation",
                    "icon": "↻",
                    "tools": [
                        "Python",
                        "Jupyter Notebook",
                        "Git / GitHub",
                        "APIs",
                        "VBA",
                        "Scripting",
                    ],
                },
            ],
        },
        "projects": {
            "eyebrow": "Projects",
            "title": "Projects and applied studies",
            "subtitle": "Examples of practical applications in dashboards, automation, data quality and analytical studies.",
            "problem": "Problem",
            "insights": "Insights",
            "impact": "Impact",
            "items": [
                {
                    "title": "Business Indicators Dashboard",
                    "emoji": "📊",
                    "problem": "The team needed clearer KPI monitoring with less dependence on manual controls.",
                    "insights": "Structuring the data and KPIs made the analysis faster, more standardized and visually clearer.",
                    "impact": "The solution improved result reading and supported more consistent monitoring of metrics.",
                    "tools": ["Power BI", "SQL", "DAX", "Excel"],
                    "link": "#",
                },
                {
                    "title": "Python Routine Automation",
                    "emoji": "🔄",
                    "problem": "Part of the operational work depended on repetitive tasks with high manual execution time.",
                    "insights": "By mapping the process steps, it was possible to identify standardization, validation and automation opportunities.",
                    "impact": "Automation reduced rework, increased productivity and improved delivery reliability.",
                    "tools": ["Python", "Pandas", "Excel", "Automation"],
                    "link": "#",
                },
                {
                    "title": "Data Quality Study",
                    "emoji": "🔍",
                    "problem": "Datasets with inconsistencies and incomplete fields affected reports and later interpretations.",
                    "insights": "The analysis revealed incorrect filling patterns, missing values and low-reliability records.",
                    "impact": "The study contributed to greater trust in the information and the creation of validation criteria.",
                    "tools": ["Python", "Pandas", "SQL", "Data Quality"],
                    "link": "#",
                },
                {
                    "title": "Applied Forecasting Study",
                    "emoji": "📈",
                    "problem": "In some contexts, anticipating demand behavior or trends can support planning.",
                    "insights": "Time analysis and simple models showed the potential of forecasting as decision support.",
                    "impact": "The project strengthened my Data Science foundation and showed how models can complement descriptive analysis.",
                    "tools": ["Python", "Scikit-learn", "Time Series", "Pandas"],
                    "link": "#",
                },
            ],
        },
        "method": {
            "eyebrow": "Method",
            "title": "My analytical method",
            "subtitle": "A visual and iterative flow to transform business needs into analysis, automation or practical solutions.",
            "note": "Hover over the steps to highlight the flow.",
            "principles_title": "Principles that guide my work",
            "steps": [
                ("🎯", "Problem", "Understand the need, the business context and the objective of the analysis."),
                ("🗂️", "Data", "Map data sources, structure, quality and information availability."),
                ("🧪", "Hypotheses", "Define questions, metrics and the analytical approach to investigate the problem."),
                ("🔧", "Treatment", "Clean, transform and organize the data for analysis or modeling."),
                ("📊", "Analysis", "Explore patterns, test hypotheses and build visualizations or models."),
                ("✅", "Delivery", "Translate results into insights, dashboards, automation or practical recommendations."),
            ],
            "principles": [
                ("Business before tools", "Technology should serve the real problem, not the opposite."),
                ("Reliable data first", "Before analyzing or modeling, it is necessary to ensure consistency and understanding of the dataset."),
                ("Clarity in communication", "An analysis only creates value when it can be understood and used by decision-makers."),
                ("Automate what makes sense", "Productivity gains appear when recurring tasks are well-structured and automated."),
                ("Continuous learning", "My growth in data is built through study, practice and constant improvement."),
                ("Practical solutions", "The final goal is always to generate something usable: insight, process, dashboard or real improvement."),
            ],
        },
        "experience": {
            "eyebrow": "Experience",
            "title": "Professional journey",
            "subtitle": "A path built through study, applied practice and direct work in Automation and Business Intelligence.",
            "items": [
                {
                    "role": "Automation and Business Intelligence Intern",
                    "company": "Current Company",
                    "period": "Feb 2026 – Present",
                    "bullets": [
                        "Dedicated work in the data area, focused on process automation and Business Intelligence.",
                        "Support in building and maintaining reports, dashboards and indicators for result tracking.",
                        "Use of analytical tools and routines to organize data, improve flows and support decisions.",
                        "Continuous development of skills in data analysis, visualization, automation and information structuring.",
                    ],
                },
                {
                    "role": "Previous experiences with applied use of data",
                    "company": "Other companies",
                    "period": "Before Feb 2026",
                    "bullets": [
                        "Applied data in professional activities, even outside formally dedicated data roles.",
                        "Supported controls, reporting, information organization and analyses for operational and managerial support.",
                        "Worked with process improvement, KPI monitoring and practical data use in business contexts.",
                        "Built the foundation that supported the transition into a role directly focused on Automation and BI.",
                    ],
                },
            ],
        },
        "contact": {
            "eyebrow": "Contact",
            "title": "Let’s talk",
            "subtitle": "Available for learning opportunities, internships, projects and connections in the data field.",
            "intro_1": (
                "I am continuously developing in the Data field, focused on Automation, BI and analytics. "
                "I am interested in opportunities that allow me to grow technically and generate real impact with data."
            ),
            "intro_2": (
                "If you are looking for someone with a strong technical foundation, willingness to learn, analytical thinking and dedication, "
                "it will be a pleasure to talk."
            ),
            "cta_title": "Let’s talk about data?",
            "cta_text": "I am open to connections, opportunities and projects in Automation, BI and Data Analysis.",
            "items": [
                ("✉️", "Email", "renanbritto.py@gmail.com", "mailto:renanbritto.py@gmail.com"),
                ("💼", "LinkedIn", "linkedin.com/in/renan-britto-7b3728212/", "https://www.linkedin.com/in/renan-britto-7b3728212/"),
                ("🐙", "GitHub", "github.com/Renanbritto", "https://github.com/Renanbritto"),
            ],
        },
        "footer": "Renan Britto · Portfólio de Dados · 2026",
    },
}


# ─────────────────────────────────────────────
# CSS
# ─────────────────────────────────────────────
def inject_css():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@300;400;500;600;700&display=swap');

        :root {
            --bg-0: #eef4fb;
            --bg-1: #e8f0fb;
            --bg-2: #dfeafb;
            --navy-1: #040911;
            --navy-2: #09111d;
            --navy-3: #0d1930;
            --blue-1: #4b8dff;
            --blue-2: #77b4ff;
            --blue-3: #b7d8ff;
            --line-blue: rgba(106, 154, 255, 0.16);
            --line-blue-strong: rgba(106, 154, 255, 0.28);
            --text-1: #0c1625;
            --text-2: #5f6e84;
            --surface-light: rgba(255,255,255,0.94);
            --header-offset: 5.25rem;
        }

        html, body, [class*="css"] {
            font-family: 'DM Sans', sans-serif;
        }

        .stApp {
            background:
                radial-gradient(circle at 12% 10%, rgba(76,141,255,0.16), transparent 24%),
                radial-gradient(circle at 82% 14%, rgba(76,141,255,0.12), transparent 28%),
                radial-gradient(circle at 50% 78%, rgba(0,176,255,0.08), transparent 24%),
                linear-gradient(180deg, var(--bg-0) 0%, var(--bg-1) 36%, var(--bg-2) 100%);
        }

        [data-testid="stAppViewContainer"] {
            background:
                linear-gradient(180deg, rgba(255,255,255,0.38) 0%, rgba(255,255,255,0.18) 100%);
        }

        [data-testid="stHeader"] {
            background:
                radial-gradient(circle at 14% 50%, rgba(76,141,255,0.18), transparent 22%),
                linear-gradient(180deg, rgba(9,17,29,0.94) 0%, rgba(12,22,36,0.88) 100%);
            backdrop-filter: blur(12px);
            border-bottom: 1px solid rgba(106,154,255,0.18);
        }

        [data-testid="stHeader"] * {
            color: #e8f2ff !important;
        }

        [data-testid="stToolbar"] {
            color: #e8f2ff !important;
        }

        [data-testid="stDecoration"] {
            background: linear-gradient(90deg, #4b8dff 0%, #77b4ff 100%);
        }

        [data-testid="stMainBlockContainer"] {
            position: relative;
            padding-top: var(--header-offset);
        }

        [data-testid="stMainBlockContainer"]::before {
            content: "";
            position: absolute;
            inset: 0 0 auto 0;
            height: 420px;
            pointer-events: none;
            background:
                radial-gradient(circle at 20% 16%, rgba(76,141,255,0.16), transparent 24%),
                radial-gradient(circle at 78% 12%, rgba(76,141,255,0.14), transparent 22%),
                linear-gradient(180deg, rgba(9,17,28,0.03) 0%, transparent 100%);
            z-index: 0;
        }

        [data-testid="stMainBlockContainer"] > div {
            position: relative;
            z-index: 1;
        }

        html,
        body {
            scroll-behavior: smooth;
            scroll-snap-type: y proximity;
            scroll-padding-top: var(--header-offset);
        }

        [data-testid="stAppViewContainer"],
        [data-testid="stMain"],
        section.main {
            scroll-snap-type: y proximity;
            scroll-behavior: smooth;
            scroll-padding-top: var(--header-offset);
        }

        .section-anchor {
            display: block;
            position: relative;
            top: calc(var(--header-offset) * -1);
            scroll-margin-top: var(--header-offset);
        }

        .st-key-page_home,
        .st-key-page_about,
        .st-key-page_skills,
        .st-key-page_projects,
        .st-key-page_method,
        .st-key-page_experience,
        .st-key-page_contact {
            min-height: calc(100vh - var(--header-offset));
            scroll-snap-align: start;
            scroll-snap-stop: always;
            padding-top: 1.75rem;
            padding-bottom: 1.25rem;
            box-sizing: border-box;
        }

        .st-key-page_home {
            display: block;
            padding-top: 0.35rem;
        }

        .st-key-page_about,
        .st-key-page_skills,
        .st-key-page_projects,
        .st-key-page_method,
        .st-key-page_experience,
        .st-key-page_contact {
            border-top: 1px solid rgba(106,154,255,0.14);
        }

        .page-status-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 18px;
            flex-wrap: wrap;
            padding: 16px 18px;
            margin-bottom: 22px;
            border-radius: 18px;
            background: rgba(255,255,255,0.78);
            border: 1px solid rgba(106,154,255,0.16);
            box-shadow:
                0 16px 34px rgba(13, 24, 40, 0.05),
                inset 0 1px 0 rgba(255,255,255,0.55);
            backdrop-filter: blur(10px);
        }

        .page-status-label {
            font-size: 0.68rem;
            letter-spacing: 0.18em;
            text-transform: uppercase;
            color: #4b8dff;
            font-weight: 800;
            margin-bottom: 6px;
        }

        .page-status-current {
            color: #0d1726;
            font-size: 1rem;
            font-weight: 700;
        }

        .page-status-hints {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }

        .page-status-pill {
            display: inline-flex;
            align-items: center;
            padding: 8px 14px;
            border-radius: 999px;
            font-size: 0.76rem;
            font-weight: 700;
            color: #35598a;
            background: rgba(89,143,255,0.08);
            border: 1px solid rgba(106,154,255,0.16);
        }

        .sidebar-nav {
            display: flex;
            flex-direction: column;
            gap: 8px;
        }

        .sidebar-link {
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 10px 0;
            color: #E8EEF8 !important;
            text-decoration: none !important;
            font-size: 0.92rem;
            letter-spacing: 0.04em;
            text-transform: uppercase;
            transition: color 0.18s ease, transform 0.18s ease;
        }

        .sidebar-link:hover {
            color: #9dcbff !important;
            transform: translateX(4px);
        }

        [data-testid="stSidebar"] {
            background:
                radial-gradient(circle at top right, rgba(76,141,255,0.14), transparent 28%),
                linear-gradient(180deg, #07101a 0%, #0c1622 100%);
            border-right: 1px solid rgba(106,154,255,0.10);
        }

        [data-testid="stSidebar"] * {
            color: #E8EEF8 !important;
        }

        div[data-testid="stRadio"] label {
            transition: all 0.2s ease;
        }

        div[data-testid="stRadio"] label:has(input[aria-checked="true"]) {
            font-weight: 700;
        }

        [data-testid="stSidebar"] .stRadio label {
            font-size: 0.92rem;
            letter-spacing: 0.04em;
            text-transform: uppercase;
            padding: 6px 0;
            cursor: pointer;
        }

        [data-testid="stSidebar"] .stRadio label:hover {
            color: #9dcbff !important;
        }

        [data-testid="stHorizontalBlock"] div[data-testid="stRadio"] > div {
            justify-content: flex-end;
            gap: 10px;
            padding-top: 8px;
        }

        [data-testid="stHorizontalBlock"] div[data-testid="stRadio"] label {
            background: rgba(255,255,255,0.72);
            border: 1px solid rgba(106,154,255,0.16);
            padding: 8px 14px !important;
            border-radius: 999px;
            min-width: 52px;
            min-height: 44px;
            justify-content: center;
            box-shadow: 0 8px 18px rgba(10, 18, 30, 0.05);
        }

        [data-testid="stHorizontalBlock"] div[data-testid="stRadio"] label:has(input[aria-checked="true"]) {
            background: linear-gradient(135deg, #4b8dff 0%, #77b4ff 100%);
            border-color: rgba(76,141,255,0.55);
            color: #ffffff !important;
            box-shadow: 0 10px 24px rgba(76,141,255,0.24);
        }

        [data-testid="stHorizontalBlock"] .stRadio label {
            text-transform: none !important;
        }

        [data-testid="stHorizontalBlock"] {
            margin-top: 6px;
            margin-bottom: 6px;
        }

        h1, h2, h3 {
            font-family: 'DM Serif Display', serif !important;
            color: var(--text-1) !important;
        }

        .hero-wrapper {
            position: relative;
            overflow: hidden;
            background:
                linear-gradient(135deg, var(--navy-1) 0%, var(--navy-2) 36%, var(--navy-3) 100%);
            border: 1px solid rgba(103, 162, 255, 0.16);
            border-radius: 28px;
            padding: 74px 64px;
            margin-bottom: 40px;
            box-shadow:
                0 32px 80px rgba(6, 10, 18, 0.22),
                0 0 0 1px rgba(120, 170, 255, 0.03),
                inset 0 1px 0 rgba(255,255,255,0.03);
        }

        .hero-bg {
            position: absolute;
            inset: 0;
            pointer-events: none;
            z-index: 0;
        }

        .hero-glow {
            position: absolute;
            border-radius: 999px;
            filter: blur(34px);
            opacity: 0.30;
            mix-blend-mode: screen;
        }

        .hero-glow-1 {
            width: 440px;
            height: 440px;
            top: -120px;
            right: -60px;
            background: radial-gradient(circle, rgba(50,120,255,0.58) 0%, rgba(50,120,255,0.10) 55%, transparent 74%);
            animation: heroFloatOne 11s ease-in-out infinite;
        }

        .hero-glow-2 {
            width: 340px;
            height: 340px;
            left: -90px;
            bottom: -110px;
            background: radial-gradient(circle, rgba(0,180,255,0.26) 0%, rgba(0,180,255,0.07) 52%, transparent 72%);
            animation: heroFloatTwo 13s ease-in-out infinite;
        }

        .hero-grid {
            position: absolute;
            inset: 0;
            background-image:
                linear-gradient(rgba(96, 143, 220, 0.08) 1px, transparent 1px),
                linear-gradient(90deg, rgba(96, 143, 220, 0.08) 1px, transparent 1px);
            background-size: 42px 42px;
            opacity: 0.18;
            mask-image: radial-gradient(circle at center, rgba(0,0,0,1) 36%, rgba(0,0,0,0.22) 82%, transparent 100%);
            animation: heroGridShift 18s linear infinite;
        }

        .hero-scan {
            position: absolute;
            inset: -10%;
            background: linear-gradient(
                115deg,
                transparent 0%,
                transparent 44%,
                rgba(130, 180, 255, 0.06) 50%,
                transparent 56%,
                transparent 100%
            );
            animation: heroScan 10s linear infinite;
        }

        .hero-particles {
            position: absolute;
            inset: 0;
            background-image:
                radial-gradient(circle at 12% 22%, rgba(132,188,255,0.28) 0 1.5px, transparent 2px),
                radial-gradient(circle at 28% 68%, rgba(132,188,255,0.20) 0 1.5px, transparent 2px),
                radial-gradient(circle at 48% 38%, rgba(132,188,255,0.16) 0 1.5px, transparent 2px),
                radial-gradient(circle at 64% 18%, rgba(132,188,255,0.20) 0 1.5px, transparent 2px),
                radial-gradient(circle at 76% 58%, rgba(132,188,255,0.22) 0 1.5px, transparent 2px),
                radial-gradient(circle at 90% 30%, rgba(132,188,255,0.18) 0 1.5px, transparent 2px);
            animation: heroParticles 14s ease-in-out infinite;
            opacity: 0.7;
        }

        .hero-content {
            position: relative;
            z-index: 2;
            display: grid;
            grid-template-columns: minmax(0, 1.25fr) minmax(290px, 0.75fr);
            gap: 34px;
            align-items: stretch;
        }

        .hero-copy {
            max-width: 820px;
        }

        .hero-eyebrow {
            font-size: 0.78rem;
            letter-spacing: 0.22em;
            text-transform: uppercase;
            color: #84baff;
            font-weight: 700;
            margin-bottom: 18px;
        }

        .hero-name {
            font-family: 'DM Serif Display', serif;
            font-size: clamp(2.8rem, 5vw, 4.5rem);
            color: #f8fbff;
            line-height: 1.02;
            margin: 0 0 14px 0;
            text-shadow: 0 0 18px rgba(118, 170, 255, 0.08);
        }

        .hero-title {
            font-size: 1.26rem;
            color: #bdd9ff;
            font-weight: 600;
            margin-bottom: 24px;
            max-width: 760px;
        }

        .hero-summary {
            font-size: 1.03rem;
            color: #d1d9e7;
            line-height: 1.9;
            max-width: 760px;
            margin-bottom: 34px;
        }

        .hero-stack {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 34px;
        }

        .stack-chip {
            background: rgba(12, 22, 35, 0.82);
            border: 1px solid rgba(124, 170, 255, 0.22);
            color: #dceaff;
            padding: 8px 16px;
            border-radius: 999px;
            font-size: 0.82rem;
            font-weight: 600;
            letter-spacing: 0.03em;
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.03);
            transition: transform 0.2s ease, border-color 0.2s ease, background 0.2s ease;
        }

        .stack-chip:hover {
            transform: translateY(-2px);
            border-color: rgba(124, 170, 255, 0.42);
            background: rgba(18, 31, 51, 0.96);
        }

        .hero-cta-row {
            display: flex;
            gap: 14px;
            flex-wrap: wrap;
        }

        .cta-btn {
            display: inline-block;
            padding: 13px 28px;
            border-radius: 12px;
            font-size: 0.9rem;
            font-weight: 700;
            letter-spacing: 0.04em;
            text-decoration: none;
            transition: transform 0.2s ease, opacity 0.2s ease, border-color 0.2s ease, background 0.2s ease;
        }

        .cta-btn:hover {
            transform: translateY(-2px);
            opacity: 0.96;
        }

        .cta-primary {
            background: linear-gradient(135deg, #86b8ff 0%, #4d8fff 100%);
            color: #07111d;
            box-shadow: 0 10px 24px rgba(76, 141, 255, 0.24);
        }

        .cta-secondary {
            background: rgba(12, 20, 31, 0.52);
            border: 1px solid rgba(124, 170, 255, 0.24);
            color: #d9e8ff;
        }

        .hero-panel {
            position: relative;
            z-index: 2;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            gap: 18px;
            padding: 24px;
            border-radius: 24px;
            background:
                linear-gradient(180deg, rgba(13, 22, 36, 0.72) 0%, rgba(8, 14, 23, 0.92) 100%);
            border: 1px solid rgba(123, 170, 255, 0.14);
            box-shadow:
                inset 0 1px 0 rgba(255,255,255,0.03),
                0 18px 40px rgba(3, 8, 18, 0.18);
            backdrop-filter: blur(6px);
        }

        .hero-panel-label {
            font-size: 0.72rem;
            text-transform: uppercase;
            letter-spacing: 0.18em;
            color: #85bcff;
            font-weight: 700;
        }

        .hero-panel-value {
            font-family: 'DM Serif Display', serif;
            font-size: 1.78rem;
            color: #f6f9ff;
            line-height: 1.1;
            margin-top: 6px;
            margin-bottom: 8px;
        }

        .hero-panel-text {
            color: #aab8cf;
            font-size: 0.88rem;
            line-height: 1.72;
        }

        .hero-panel-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
        }

        .hero-panel-mini {
            padding: 14px 12px;
            border-radius: 16px;
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(120, 170, 255, 0.10);
            transition: transform 0.18s ease, border-color 0.18s ease, background 0.18s ease;
        }

        .hero-panel-mini:hover {
            transform: translateY(-2px);
            border-color: rgba(120, 170, 255, 0.22);
            background: rgba(255,255,255,0.05);
        }

        .hero-panel-mini strong {
            display: block;
            color: #f6f9ff;
            font-size: 1rem;
            margin-bottom: 4px;
        }

        .hero-panel-mini span {
            color: #97a9c4;
            font-size: 0.76rem;
        }

        .card,
        .metric-box,
        .exp-card,
        .contact-item {
            background:
                linear-gradient(180deg, rgba(255,255,255,0.96) 0%, rgba(247,250,255,0.96) 100%);
            border: 1px solid rgba(106,154,255,0.14);
            border-radius: 14px;
            box-shadow:
                0 16px 34px rgba(13, 24, 40, 0.05),
                inset 0 1px 0 rgba(255,255,255,0.55);
        }

        .card {
            padding: 28px;
            height: 100%;
            transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
        }

        .card:hover,
        .exp-card:hover,
        .contact-item:hover {
            border-color: rgba(106,154,255,0.28);
            box-shadow:
                0 20px 38px rgba(13, 24, 40, 0.07),
                inset 0 1px 0 rgba(255,255,255,0.58);
        }

        .card-accent {
            border-left: 4px solid #6ca6ff;
        }

        .metric-box {
            padding: 24px 20px;
            text-align: center;
            backdrop-filter: blur(10px);
        }

        .metric-number {
            font-family: 'DM Serif Display', serif;
            font-size: 2.2rem;
            color: #0f1a2c;
            line-height: 1;
            margin-bottom: 6px;
        }

        .metric-label {
            font-size: 0.78rem;
            color: #6b7790;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            font-weight: 600;
        }

        .tech-tag {
            display: inline-block;
            background: rgba(89, 143, 255, 0.06);
            border: 1px solid rgba(106,154,255,0.16);
            color: #29405f;
            padding: 4px 12px;
            border-radius: 6px;
            font-size: 0.78rem;
            font-weight: 500;
            margin: 3px 3px 3px 0;
            transition: transform 0.18s ease, background 0.18s ease, border-color 0.18s ease;
        }

        .tech-tag:hover {
            transform: translateY(-2px);
            background: rgba(89, 143, 255, 0.11);
            border-color: rgba(106,154,255,0.30);
        }

        .section-divider {
            border: none;
            border-top: 1px solid rgba(106,154,255,0.16);
            margin: 48px 0 40px 0;
        }

        .section-eyebrow {
            font-size: 0.72rem;
            letter-spacing: 0.22em;
            text-transform: uppercase;
            color: #4b8dff;
            font-weight: 800;
            margin-bottom: 6px;
        }

        .section-title {
            font-family: 'DM Serif Display', serif;
            font-size: 2rem;
            color: #0d1726;
            margin-bottom: 8px;
        }

        .section-subtitle {
            color: #667387;
            font-size: 0.96rem;
            margin-bottom: 32px;
            line-height: 1.75;
            max-width: 760px;
        }

        .projects-showcase {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 18px;
        }

        .project-card {
            position: relative;
            overflow: hidden;
            background:
                radial-gradient(circle at top right, rgba(119,180,255,0.12), transparent 32%),
                linear-gradient(180deg, rgba(255,255,255,0.98) 0%, rgba(246,249,255,0.98) 100%);
            border: 1px solid rgba(106,154,255,0.14);
            border-radius: 20px;
            padding: 22px;
            box-shadow:
                0 18px 34px rgba(13, 24, 40, 0.05),
                inset 0 1px 0 rgba(255,255,255,0.56);
            transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
        }

        .project-card:hover {
            transform: translateY(-4px);
            border-color: rgba(106,154,255,0.28);
            box-shadow:
                0 24px 40px rgba(13, 24, 40, 0.08),
                inset 0 1px 0 rgba(255,255,255,0.58);
        }

        .project-card-head {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 18px;
        }

        .project-card-emoji {
            width: 48px;
            height: 48px;
            border-radius: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: linear-gradient(135deg, #0b1524 0%, #14345f 100%);
            color: #ffffff;
            font-size: 1.3rem;
            box-shadow: 0 10px 24px rgba(10, 18, 30, 0.12);
        }

        .project-card-title {
            font-family: 'DM Serif Display', serif;
            font-size: 1.28rem;
            color: #111111;
            line-height: 1.15;
        }

        .project-block {
            margin-bottom: 14px;
        }

        .project-kicker {
            font-size: 0.7rem;
            text-transform: uppercase;
            letter-spacing: 0.12em;
            color: #4b8dff;
            font-weight: 800;
            margin-bottom: 6px;
        }

        .project-copy {
            font-size: 0.88rem;
            color: #445168;
            line-height: 1.68;
        }

        .project-footer {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 12px;
            flex-wrap: wrap;
            margin-top: 14px;
        }

        .project-link {
            font-size: 0.82rem;
            font-weight: 700;
            color: #15407f;
            text-decoration: none;
            background: rgba(89,143,255,0.08);
            border: 1px solid rgba(106,154,255,0.18);
            padding: 9px 18px;
            border-radius: 10px;
            letter-spacing: 0.04em;
            transition: transform 0.18s ease, background 0.18s ease, border-color 0.18s ease;
        }

        .project-link:hover {
            transform: translateY(-2px);
            background: rgba(89,143,255,0.12);
            border-color: rgba(106,154,255,0.28);
        }

        .principles-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 16px;
        }

        .exp-card {
            padding: 28px;
            margin-bottom: 16px;
        }

        .exp-company {
            font-weight: 700;
            color: #111111;
            font-size: 1rem;
        }

        .exp-role {
            color: #4b8dff;
            font-size: 0.88rem;
            font-weight: 600;
            margin: 2px 0 4px 0;
        }

        .exp-period {
            color: #8090a8;
            font-size: 0.78rem;
            margin-bottom: 14px;
        }

        .contact-item {
            display: flex;
            align-items: center;
            gap: 14px;
            padding: 18px 20px;
            margin-bottom: 12px;
            text-decoration: none;
            color: #111111;
            transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
        }

        .contact-item:hover {
            transform: translateY(-2px);
        }

        .skills-shell {
            position: relative;
            padding: 8px 2px 18px 2px;
            margin-bottom: 14px;
        }

        .skills-flow {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 14px;
            width: 100%;
            padding: 6px 2px 10px 2px;
        }

        .skills-node {
            position: relative;
            width: min(100%, 760px);
            min-height: 220px;
            background:
                radial-gradient(circle at top right, rgba(119,180,255,0.14), transparent 30%),
                linear-gradient(180deg, rgba(255,255,255,0.98) 0%, rgba(246,249,255,0.98) 100%);
            border: 1px solid rgba(106,154,255,0.14);
            border-radius: 18px;
            padding: 22px 20px 20px 20px;
            box-shadow: 0 14px 30px rgba(17,17,17,0.05);
            transition: transform 0.22s ease, box-shadow 0.22s ease, border-color 0.22s ease;
            overflow: hidden;
        }

        .skills-node::before {
            content: "";
            position: absolute;
            inset: 0;
            background: linear-gradient(135deg, rgba(119,180,255,0.08), transparent 45%);
            opacity: 0;
            transition: opacity 0.22s ease;
            pointer-events: none;
        }

        .skills-node:hover {
            transform: translateY(-8px);
            border-color: rgba(106,154,255,0.34);
            box-shadow: 0 22px 40px rgba(17,17,17,0.10);
        }

        .skills-node:hover::before {
            opacity: 1;
        }

        .skills-node-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
            margin-bottom: 18px;
        }

        .skills-node-title {
            font-family: 'DM Serif Display', serif;
            font-size: 1.22rem;
            color: #111111;
            line-height: 1.2;
            max-width: 520px;
        }

        .skills-node-icon {
            width: 48px;
            height: 48px;
            border-radius: 14px;
            background: linear-gradient(135deg, #0b1524 0%, #132541 100%);
            color: #F7F7F5;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.2rem;
            box-shadow: 0 10px 20px rgba(17,17,17,0.12);
            transition: transform 0.22s ease;
            flex-shrink: 0;
        }

        .skills-node:hover .skills-node-icon {
            transform: rotate(-6deg) scale(1.06);
        }

        .skills-tags-wrap {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }

        .skills-tag {
            display: inline-flex;
            align-items: center;
            padding: 7px 12px;
            border-radius: 999px;
            border: 1px solid rgba(106,154,255,0.15);
            background: rgba(89, 143, 255, 0.06);
            color: #3f5067;
            font-size: 0.8rem;
            font-weight: 500;
            transition: transform 0.18s ease, background 0.18s ease, border-color 0.18s ease;
        }

        .skills-tag:hover {
            transform: translateY(-2px);
            background: rgba(89, 143, 255, 0.10);
            border-color: rgba(106,154,255,0.30);
        }

        .skills-connector {
            position: relative;
            width: 100%;
            height: 56px;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .skills-connector::before {
            content: "";
            width: 3px;
            height: 100%;
            border-radius: 999px;
            background: linear-gradient(
                180deg,
                rgba(106,154,255,0.10) 0%,
                rgba(106,154,255,0.75) 50%,
                rgba(106,154,255,0.10) 100%
            );
            background-size: 100% 220%;
            animation: flowMoveVertical 4s linear infinite;
        }

        .skills-connector::after {
            content: "◆";
            position: absolute;
            left: 50%;
            bottom: -2px;
            transform: translateX(-50%);
            color: #4b8dff;
            font-size: 1rem;
            text-shadow: 0 4px 10px rgba(17,17,17,0.08);
        }

        .skills-note {
            margin-top: 8px;
            color: #667387;
            font-size: 0.8rem;
            letter-spacing: 0.02em;
        }

        .method-shell {
            position: relative;
            overflow-x: auto;
            padding: 8px 2px 18px 2px;
            margin-bottom: 12px;
        }

        .method-shell::-webkit-scrollbar {
            height: 8px;
        }

        .method-shell::-webkit-scrollbar-thumb {
            background: rgba(106,154,255,0.28);
            border-radius: 999px;
        }

        .method-flow {
            display: flex;
            align-items: stretch;
            gap: 14px;
            min-width: max-content;
            padding: 6px 2px 10px 2px;
        }

        .method-node {
            position: relative;
            width: 230px;
            min-height: 220px;
            background:
                radial-gradient(circle at top right, rgba(119,180,255,0.14), transparent 30%),
                linear-gradient(180deg, rgba(255,255,255,0.98) 0%, rgba(246,249,255,0.98) 100%);
            border: 1px solid rgba(106,154,255,0.14);
            border-radius: 18px;
            padding: 20px 18px 18px 18px;
            box-shadow: 0 14px 30px rgba(17,17,17,0.05);
            transition: transform 0.22s ease, box-shadow 0.22s ease, border-color 0.22s ease;
            overflow: hidden;
        }

        .method-node::before {
            content: "";
            position: absolute;
            inset: 0;
            background: linear-gradient(135deg, rgba(119,180,255,0.08), transparent 45%);
            opacity: 0;
            transition: opacity 0.22s ease;
            pointer-events: none;
        }

        .method-node:hover {
            transform: translateY(-8px);
            border-color: rgba(106,154,255,0.34);
            box-shadow: 0 22px 40px rgba(17,17,17,0.10);
        }

        .method-node:hover::before {
            opacity: 1;
        }

        .method-node-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 18px;
        }

        .method-step-badge {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            min-width: 42px;
            height: 42px;
            border-radius: 999px;
            background: linear-gradient(135deg, #0b1524 0%, #14345f 100%);
            color: #F7F7F5;
            font-size: 0.82rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            box-shadow: 0 8px 20px rgba(17,17,17,0.14);
        }

        .method-node-icon {
            font-size: 1.7rem;
            line-height: 1;
            transition: transform 0.22s ease;
        }

        .method-node:hover .method-node-icon {
            transform: scale(1.12) rotate(-4deg);
        }

        .method-node-title {
            font-family: 'DM Serif Display', serif;
            font-size: 1.2rem;
            color: #111111;
            margin-bottom: 8px;
        }

        .method-node-desc {
            color: #666660;
            font-size: 0.85rem;
            line-height: 1.65;
        }

        .method-connector {
            position: relative;
            min-width: 88px;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .method-connector::before {
            content: "";
            width: 100%;
            height: 3px;
            border-radius: 999px;
            background: linear-gradient(
                90deg,
                rgba(106,154,255,0.10) 0%,
                rgba(106,154,255,0.75) 50%,
                rgba(106,154,255,0.10) 100%
            );
            background-size: 220% 100%;
            animation: methodFlowMove 4s linear infinite;
        }

        .method-connector::after {
            content: "→";
            position: absolute;
            right: -2px;
            top: 50%;
            transform: translateY(-50%);
            width: 28px;
            height: 28px;
            border-radius: 999px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: #F7F9FD;
            border: 1px solid rgba(106,154,255,0.20);
            color: #4b8dff;
            font-weight: 700;
            box-shadow: 0 6px 16px rgba(17,17,17,0.06);
        }

        .method-note {
            margin-top: 8px;
            color: #667387;
            font-size: 0.8rem;
            letter-spacing: 0.02em;
        }

        .principle-mini-card {
            background: linear-gradient(180deg, #FCFDFF 0%, #F3F8FF 100%);
            border: 1px solid rgba(106,154,255,0.14);
            border-radius: 14px;
            padding: 18px;
            transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
        }

        .principle-mini-card:hover {
            transform: translateY(-4px);
            border-color: rgba(106,154,255,0.28);
            box-shadow: 0 12px 24px rgba(17,17,17,0.05);
        }

        .experience-shell {
            position: relative;
            padding: 8px 2px 18px 2px;
            margin-bottom: 14px;
        }

        .experience-timeline {
            position: relative;
            display: flex;
            flex-direction: column;
            gap: 18px;
            width: 100%;
        }

        .experience-timeline::before {
            content: "";
            position: absolute;
            left: 42px;
            top: 18px;
            bottom: 18px;
            width: 4px;
            border-radius: 999px;
            background: linear-gradient(
                180deg,
                rgba(106,154,255,0.18) 0%,
                rgba(106,154,255,0.95) 48%,
                rgba(106,154,255,0.18) 100%
            );
            box-shadow: 0 0 18px rgba(76,141,255,0.10);
        }

        .experience-item {
            position: relative;
            display: grid;
            grid-template-columns: 86px minmax(0, 1fr);
            gap: 10px;
            align-items: start;
            width: 100%;
        }

        .experience-item::before {
            content: "";
            position: absolute;
            left: 68px;
            top: 25px;
            width: 22px;
            height: 3px;
            border-radius: 999px;
            background: linear-gradient(
                90deg,
                rgba(106,154,255,0.92) 0%,
                rgba(106,154,255,0.26) 100%
            );
        }

        .experience-rail {
            position: relative;
            display: flex;
            justify-content: center;
            padding-top: 0;
            z-index: 2;
        }

        .experience-node-wrap {
            position: relative;
            width: 62px;
            display: flex;
            justify-content: center;
        }

        .experience-node-wrap.current::before {
            content: "";
            position: absolute;
            width: 62px;
            height: 62px;
            border-radius: 999px;
            background: radial-gradient(circle, rgba(76,141,255,0.20) 0%, rgba(76,141,255,0.04) 58%, transparent 72%);
            animation: experiencePulse 2.8s ease-in-out infinite;
        }

        .experience-node {
            position: relative;
            z-index: 2;
            width: 52px;
            height: 52px;
            border-radius: 18px;
            background: linear-gradient(135deg, #0b1524 0%, #14345f 100%);
            color: #F7F9FF;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.3rem;
            box-shadow: 0 12px 24px rgba(10, 18, 30, 0.16);
            border: 1px solid rgba(106,154,255,0.16);
            transition: transform 0.22s ease, box-shadow 0.22s ease;
        }

        .experience-item:hover .experience-node {
            transform: translateY(-4px) scale(1.04);
            box-shadow: 0 16px 28px rgba(10, 18, 30, 0.20);
        }

        .experience-node.current {
            background: linear-gradient(135deg, #4b8dff 0%, #77b4ff 100%);
            color: #06101a;
            box-shadow:
                0 14px 30px rgba(76,141,255,0.28),
                0 0 0 4px rgba(76,141,255,0.12);
        }

        .experience-node-order {
            position: absolute;
            right: -6px;
            bottom: -6px;
            min-width: 24px;
            height: 24px;
            border-radius: 999px;
            background: #ffffff;
            color: #0d1930;
            border: 1px solid rgba(106,154,255,0.18);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.65rem;
            font-weight: 800;
            letter-spacing: 0.06em;
            box-shadow: 0 8px 18px rgba(17,17,17,0.08);
        }

        .experience-connector {
            display: none;
        }

        .experience-card-modern {
            position: relative;
            overflow: hidden;
            background:
                radial-gradient(circle at top right, rgba(119,180,255,0.14), transparent 32%),
                linear-gradient(180deg, rgba(255,255,255,0.98) 0%, rgba(246,249,255,0.98) 100%);
            border: 1px solid rgba(106,154,255,0.14);
            border-radius: 22px;
            padding: 24px 24px 22px 24px;
            box-shadow:
                0 18px 34px rgba(13, 24, 40, 0.05),
                inset 0 1px 0 rgba(255,255,255,0.56);
            transition: transform 0.22s ease, border-color 0.22s ease, box-shadow 0.22s ease;
        }

        .experience-card-modern::before {
            content: "";
            position: absolute;
            inset: 0;
            background: linear-gradient(135deg, rgba(119,180,255,0.08), transparent 44%);
            opacity: 0;
            transition: opacity 0.22s ease;
            pointer-events: none;
        }

        .experience-card-modern:hover {
            transform: translateY(-6px);
            border-color: rgba(106,154,255,0.30);
            box-shadow:
                0 24px 40px rgba(13, 24, 40, 0.08),
                inset 0 1px 0 rgba(255,255,255,0.60);
        }

        .experience-card-modern:hover::before {
            opacity: 1;
        }

        .experience-card-modern.current {
            border-color: rgba(76,141,255,0.28);
            box-shadow:
                0 26px 44px rgba(76,141,255,0.10),
                inset 0 1px 0 rgba(255,255,255,0.62);
        }

        .experience-growth-bar {
            position: absolute;
            left: 0;
            top: 0;
            bottom: 0;
            width: 6px;
            border-radius: 22px 0 0 22px;
            background: linear-gradient(180deg, #9fd0ff 0%, #4b8dff 55%, #153f7d 100%);
            opacity: 0.95;
        }

        .experience-card-top {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            gap: 16px;
            flex-wrap: wrap;
            margin-bottom: 16px;
            position: relative;
            z-index: 1;
        }

        .experience-company-modern {
            font-family: 'DM Serif Display', serif;
            font-size: 1.42rem;
            color: #111111;
            line-height: 1.08;
            margin-bottom: 6px;
        }

        .experience-role-modern {
            color: #4b8dff;
            font-size: 0.94rem;
            font-weight: 800;
            letter-spacing: 0.02em;
            margin-bottom: 10px;
        }

        .experience-badge-row {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }

        .experience-badge {
            display: inline-flex;
            align-items: center;
            padding: 7px 12px;
            border-radius: 999px;
            font-size: 0.72rem;
            font-weight: 800;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            background: rgba(89,143,255,0.08);
            border: 1px solid rgba(106,154,255,0.18);
            color: #35598a;
        }

        .experience-badge.current {
            background: linear-gradient(135deg, #4b8dff 0%, #77b4ff 100%);
            border-color: rgba(76,141,255,0.48);
            color: #ffffff;
            box-shadow: 0 10px 22px rgba(76,141,255,0.22);
        }

        .experience-period-modern {
            display: inline-flex;
            align-items: center;
            padding: 10px 14px;
            border-radius: 999px;
            background: rgba(89,143,255,0.08);
            border: 1px solid rgba(106,154,255,0.18);
            color: #57749c;
            font-size: 0.8rem;
            font-weight: 700;
            white-space: nowrap;
        }

        .experience-list {
            position: relative;
            z-index: 1;
            margin: 0;
            padding-left: 20px;
        }

        .experience-list li {
            color: #445168;
            font-size: 0.9rem;
            line-height: 1.82;
            margin-bottom: 8px;
        }

        @keyframes heroFloatOne {
            0%, 100% { transform: translate3d(0, 0, 0) scale(1); }
            50% { transform: translate3d(-26px, 18px, 0) scale(1.06); }
        }

        @keyframes heroFloatTwo {
            0%, 100% { transform: translate3d(0, 0, 0) scale(1); }
            50% { transform: translate3d(22px, -16px, 0) scale(1.05); }
        }

        @keyframes heroGridShift {
            0% { transform: translate3d(0, 0, 0); }
            50% { transform: translate3d(-12px, -10px, 0); }
            100% { transform: translate3d(0, 0, 0); }
        }

        @keyframes heroScan {
            0% { transform: translateX(-24%); }
            100% { transform: translateX(24%); }
        }

        @keyframes heroParticles {
            0%, 100% { transform: translateY(0px) translateX(0px); opacity: 0.64; }
            50% { transform: translateY(-8px) translateX(6px); opacity: 0.88; }
        }

        @keyframes methodFlowMove {
            0% { background-position: 200% 0; }
            100% { background-position: -200% 0; }
        }

        @keyframes flowMoveVertical {
            0% { background-position: 0 200%; }
            100% { background-position: 0 -200%; }
        }

        @keyframes experiencePulse {
            0%, 100% { transform: scale(1); opacity: 0.9; }
            50% { transform: scale(1.08); opacity: 0.45; }
        }

        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}

        @media (max-width: 1100px) {
            .projects-showcase {
                grid-template-columns: 1fr;
            }
        }

        @media (max-width: 900px) {
            :root {
                --header-offset: 6.75rem;
            }

            [data-testid="stHeader"] {
                background:
                    radial-gradient(circle at 18% 50%, rgba(76,141,255,0.18), transparent 24%),
                    linear-gradient(180deg, rgba(9,17,29,0.96) 0%, rgba(12,22,36,0.92) 100%);
            }

            [data-testid="stMainBlockContainer"] {
                padding-top: var(--header-offset);
            }

            [data-testid="stHorizontalBlock"] div[data-testid="stRadio"] > div {
                justify-content: flex-end;
                padding-top: 12px;
            }

            [data-testid="stHorizontalBlock"] div[data-testid="stRadio"] label {
                min-height: 46px;
                padding: 10px 14px !important;
            }

            .page-status-bar {
                padding: 14px 16px;
                border-radius: 16px;
            }

            .page-status-current {
                font-size: 0.94rem;
            }

            .st-key-page_home,
            .st-key-page_about,
            .st-key-page_skills,
            .st-key-page_projects,
            .st-key-page_method,
            .st-key-page_experience,
            .st-key-page_contact {
                min-height: calc(100vh - var(--header-offset));
                padding-top: 1rem;
                padding-bottom: 0.8rem;
            }

            .st-key-page_home {
                padding-top: 0.2rem;
            }

            .hero-wrapper {
                padding: 34px 24px;
                border-radius: 22px;
            }

            .hero-content {
                grid-template-columns: 1fr;
                gap: 24px;
            }

            .hero-panel {
                padding: 18px;
            }

            .hero-panel-grid {
                grid-template-columns: 1fr 1fr;
            }

            .hero-title {
                font-size: 1.1rem;
            }

            .hero-summary {
                font-size: 0.97rem;
                line-height: 1.8;
            }

            .principles-grid {
                grid-template-columns: 1fr;
            }

            .skills-node,
            .method-node {
                width: 100%;
                min-height: auto;
            }

            .method-flow {
                flex-direction: column;
                min-width: 100%;
                gap: 10px;
            }

            .method-connector {
                min-width: 100%;
                width: 100%;
                height: 42px;
            }

            .method-connector::before {
                width: 3px;
                height: 100%;
            }

            .method-connector::after {
                right: 50%;
                top: auto;
                bottom: -4px;
                transform: translateX(50%) rotate(90deg);
            }

            .experience-timeline::before {
                left: 26px;
            }

            .experience-item {
                grid-template-columns: 52px minmax(0, 1fr);
                gap: 12px;
            }

            .experience-item::before {
                left: 44px;
                width: 16px;
            }

            .experience-rail {
                justify-content: flex-start;
            }

            .experience-node-wrap {
                width: 52px;
                justify-content: flex-start;
            }

            .experience-card-top {
                flex-direction: column;
                align-items: flex-start;
            }

            .experience-company-modern {
                font-size: 1.18rem;
            }

            .experience-period-modern {
                white-space: normal;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────
def normalize_page(page):
    if isinstance(page, list):
        page = page[0] if page else "home"

    if not isinstance(page, str):
        return "home"

    return page if page in SECTION_ORDER else "home"


def get_query_page():
    try:
        raw_page = st.query_params.get("section")
    except Exception:
        return None

    if raw_page in (None, ""):
        return None

    return normalize_page(raw_page)


def set_current_page(page):
    normalized_page = normalize_page(page)
    st.session_state["selected_page"] = normalized_page

    try:
        if st.query_params.get("section") != normalized_page:
            st.query_params["section"] = normalized_page
    except Exception:
        pass

    return normalized_page


def init_session_state():
    if "lang" not in st.session_state:
        st.session_state["lang"] = "pt"

    query_page = get_query_page()

    if "selected_page" not in st.session_state:
        st.session_state["selected_page"] = query_page or "home"
    elif query_page and st.session_state["selected_page"] != query_page:
        st.session_state["selected_page"] = query_page


def get_lang():
    init_session_state()
    return st.session_state["lang"]


def content():
    return CONTENT[get_lang()]


def render_html(html: str):
    cleaned = "\n".join(
        line.lstrip()
        for line in html.splitlines()
        if line.strip()
    )
    st.markdown(cleaned, unsafe_allow_html=True)


def render_section_header(eyebrow, title, subtitle=None):
    st.markdown(f'<div class="section-eyebrow">{eyebrow}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">{title}</div>', unsafe_allow_html=True)
    if subtitle:
        st.markdown(f'<div class="section-subtitle">{subtitle}</div>', unsafe_allow_html=True)


def render_tags(tags):
    return "".join(f'<span class="tech-tag">{tag}</span>' for tag in tags)


def section_divider():
    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)


def render_page_status(selected_key):
    current_index = SECTION_ORDER.index(selected_key)
    current_label = NAV_ITEMS[selected_key][get_lang()]
    prev_key = SECTION_ORDER[current_index - 1] if current_index > 0 else None
    next_key = SECTION_ORDER[current_index + 1] if current_index < len(SECTION_ORDER) - 1 else None

    if get_lang() == "pt":
        title = "Navegacao automatica"
        current_text = "Pagina atual"
        prev_text = "Role para cima"
        next_text = "Role para baixo"
        edge_text = "Fim da navegacao"
    else:
        title = "Automatic Navigation"
        current_text = "Current page"
        prev_text = "Scroll up"
        next_text = "Scroll down"
        edge_text = "End of navigation"

    prev_label = NAV_ITEMS[prev_key][get_lang()] if prev_key else edge_text
    next_label = NAV_ITEMS[next_key][get_lang()] if next_key else edge_text

    render_html(
        f"""
        <div class="page-status-bar">
            <div>
                <div class="page-status-label">{title}</div>
                <div class="page-status-current">{current_text}: {current_label}</div>
            </div>
            <div class="page-status-hints">
                <span class="page-status-pill">{prev_text}: {prev_label}</span>
                <span class="page-status-pill">{next_text}: {next_label}</span>
            </div>
        </div>
        """
    )


def render_scroll_navigation_script(selected_key):
    components.html(
        f"""
        <script>
        const pages = {json.dumps(SECTION_ORDER)};
        const currentPage = {json.dumps(selected_key)};
        const parentWindow = window.parent;
        const storeKey = "__portfolio_scroll_nav__";
        const edgeThreshold = 32;
        const compactThreshold = 120;
        const wheelThreshold = 80;
        const touchThreshold = 70;

        if (parentWindow[storeKey] && typeof parentWindow[storeKey].cleanup === "function") {{
            parentWindow[storeKey].cleanup();
        }}

        const navigateTo = (targetPage) => {{
            if (!targetPage) return;
            const url = new URL(parentWindow.location.href);
            url.searchParams.set("section", targetPage);
            parentWindow.location.href = url.toString();
        }};

        let locked = false;
        let wheelDelta = 0;
        let wheelResetTimer = null;
        let touchStartY = null;

        const getMetrics = () => {{
            const doc = parentWindow.document.documentElement;
            const body = parentWindow.document.body;
            const scrollingElement = parentWindow.document.scrollingElement || doc || body;
            const scrollTop = scrollingElement ? scrollingElement.scrollTop : (parentWindow.pageYOffset || 0);
            const viewportHeight = parentWindow.innerHeight || doc.clientHeight || 0;
            const fullHeight = Math.max(
                doc.scrollHeight || 0,
                body.scrollHeight || 0,
                doc.offsetHeight || 0,
                body.offsetHeight || 0
            );

            return {{
                scrollTop,
                viewportHeight,
                fullHeight,
                nearTop: scrollTop <= edgeThreshold,
                nearBottom: scrollTop + viewportHeight >= fullHeight - edgeThreshold,
                compactPage: fullHeight <= viewportHeight + compactThreshold,
            }};
        }};

        const isIgnoredTarget = (target) => {{
            if (!target || typeof target.closest !== "function") return false;

            return Boolean(
                target.closest('[data-testid="stSidebar"]') ||
                target.closest('input, textarea, select, option, button, a, [role="slider"], [contenteditable="true"]')
            );
        }};

        const maybeNavigate = (direction) => {{
            if (locked || !direction) return;

            const currentIndex = pages.indexOf(currentPage);
            if (currentIndex === -1) return;

            const metrics = getMetrics();

            if (direction > 0 && (metrics.compactPage || metrics.nearBottom) && currentIndex < pages.length - 1) {{
                locked = true;
                navigateTo(pages[currentIndex + 1]);
            }}

            if (direction < 0 && (metrics.compactPage || metrics.nearTop) && currentIndex > 0) {{
                locked = true;
                navigateTo(pages[currentIndex - 1]);
            }}
        }};

        const wheelHandler = (event) => {{
            if (locked || isIgnoredTarget(event.target)) return;

            wheelDelta += event.deltaY;

            if (wheelResetTimer) {{
                parentWindow.clearTimeout(wheelResetTimer);
            }}

            wheelResetTimer = parentWindow.setTimeout(() => {{
                wheelDelta = 0;
            }}, 180);

            if (Math.abs(wheelDelta) < wheelThreshold) return;

            maybeNavigate(wheelDelta > 0 ? 1 : -1);
            wheelDelta = 0;
        }};

        const touchStartHandler = (event) => {{
            if (isIgnoredTarget(event.target)) return;
            touchStartY = event.touches && event.touches.length ? event.touches[0].clientY : null;
        }};

        const touchEndHandler = (event) => {{
            if (locked || touchStartY === null || isIgnoredTarget(event.target)) return;

            const touch = event.changedTouches && event.changedTouches.length ? event.changedTouches[0] : null;
            if (!touch) return;

            const deltaY = touchStartY - touch.clientY;
            touchStartY = null;

            if (Math.abs(deltaY) < touchThreshold) return;

            maybeNavigate(deltaY > 0 ? 1 : -1);
        }};

        const keyHandler = (event) => {{
            if (locked || isIgnoredTarget(event.target)) return;

            if (event.key === "PageDown" || event.key === "ArrowDown") {{
                maybeNavigate(1);
            }}

            if (event.key === "PageUp" || event.key === "ArrowUp") {{
                maybeNavigate(-1);
            }}
        }};

        parentWindow.addEventListener("wheel", wheelHandler, {{ passive: true }});
        parentWindow.addEventListener("touchstart", touchStartHandler, {{ passive: true }});
        parentWindow.addEventListener("touchend", touchEndHandler, {{ passive: true }});
        parentWindow.addEventListener("keydown", keyHandler);

        parentWindow[storeKey] = {{
            cleanup: () => {{
                parentWindow.removeEventListener("wheel", wheelHandler);
                parentWindow.removeEventListener("touchstart", touchStartHandler);
                parentWindow.removeEventListener("touchend", touchEndHandler);
                parentWindow.removeEventListener("keydown", keyHandler);
            }}
        }};

        parentWindow.requestAnimationFrame(() => {{
            parentWindow.scrollTo({{ top: 0, behavior: "auto" }});
        }});
        </script>
        """,
        height=0,
        width=0,
    )


def render_scroll_to_section_script(selected_key):
    target_selector = ".st-key-page_home" if selected_key == "home" else f".st-key-page_{selected_key}"

    components.html(
        f"""
        <script>
        const parentWindow = window.parent;
        const selector = {json.dumps(target_selector)};
        const storageKey = "__portfolio_last_section__";

        const scrollToTarget = () => {{
            const target = parentWindow.document.querySelector(selector);
            if (!target) return false;

            target.scrollIntoView({{ behavior: "smooth", block: "start" }});
            parentWindow.sessionStorage.setItem(storageKey, selector);
            return true;
        }};

        const lastTarget = parentWindow.sessionStorage.getItem(storageKey);

        if (lastTarget !== selector) {{
            let attempts = 0;
            const maxAttempts = 30;

            const tryScroll = () => {{
                attempts += 1;

                if (scrollToTarget() || attempts >= maxAttempts) return;

                parentWindow.setTimeout(tryScroll, 120);
            }};

            tryScroll();
        }}
        </script>
        """,
        height=0,
        width=0,
    )


def get_experience_meta(exp, idx, total):
    role = exp["role"].lower()
    period = exp["period"].lower()

    is_current = "atual" in period or "present" in period or "current" in period

    if "business intelligence" in role or "automação" in role or "automation" in role:
        icon = "⚡"
    elif "suporte" in role or "support" in role:
        icon = "🛠️"
    elif "infra" in role or "infraestrutura" in role:
        icon = "🖧"
    elif "sales" in role or "development representative" in role or "comercial" in role:
        icon = "🚀"
    elif "logística" in role or "logistica" in role:
        icon = "📦"
    else:
        icon = "💼"

    if is_current:
        badge = "Atual" if get_lang() == "pt" else "Current"
    else:
        badge = "Base" if idx == total else "Etapa" if get_lang() == "pt" else "Stage"

    return {
        "icon": icon,
        "is_current": is_current,
        "badge": badge,
    }


def render_language_switcher():
    left, right = st.columns([8, 2])
    with right:
        st.radio(
            "Idioma / Language",
            options=list(LANG_OPTIONS.keys()),
            format_func=lambda x: LANG_OPTIONS[x]["flag"],
            horizontal=True,
            label_visibility="collapsed",
            key="lang",
        )

# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
def render_sidebar():
    init_session_state()
    current = content()
    nav_links = "".join(
        f'<a href="#{key}" target="_self" class="sidebar-link">{NAV_ITEMS[key][get_lang()]}</a>'
        for key in SECTION_ORDER
    )

    with st.sidebar:
        render_html(
            f"""
            <div style="padding: 8px 0 28px 0;">
                <div style="font-family:'DM Serif Display',serif; font-size:1.35rem; color:#F7F7F5; margin-bottom:4px;">
                    {PROFILE["name"]}
                </div>
                <div style="font-size:0.76rem; color:#84baff; letter-spacing:0.12em; text-transform:uppercase;">
                    {current["headline"]}
                </div>
                <div style="font-size:0.72rem; color:#9fb2cc; margin-top:10px;">
                    {current["location"]}
                </div>
            </div>
            <hr style="border:none;border-top:1px solid rgba(106,154,255,0.12);margin-bottom:24px;">
            """
        )

        render_html(
            f"""
            <div class="sidebar-nav">
                {nav_links}
            </div>
            """
        )

        st.markdown("<br>", unsafe_allow_html=True)
        render_html(
            f"""
            <div style="font-size:0.7rem; color:#9fb2cc; padding-top:24px; border-top:1px solid rgba(106,154,255,0.12);">
                {current["sidebar_note"]}
            </div>
            """
        )

    return "home"

# ─────────────────────────────────────────────
# SEÇÕES
# ─────────────────────────────────────────────
def render_hero():
    current = content()
    buttons = current["buttons"]
    panel = current["hero_panel"]
    stack_html = "".join(f'<span class="stack-chip">{item}</span>' for item in current["stack_items"])
    panel_cards_html = "".join(
        f"""
        <div class="hero-panel-mini">
            <strong>{title}</strong>
            <span>{subtitle}</span>
        </div>
        """
        for title, subtitle in panel["cards"]
    )

    render_html(
        f"""
        <div class="hero-wrapper">
            <div class="hero-bg">
                <div class="hero-glow hero-glow-1"></div>
                <div class="hero-glow hero-glow-2"></div>
                <div class="hero-grid"></div>
                <div class="hero-scan"></div>
                <div class="hero-particles"></div>
            </div>

            <div class="hero-content">
                <div class="hero-copy">
                    <div class="hero-eyebrow">{current["headline"]}</div>
                    <div class="hero-name">{PROFILE["name"]}</div>
                    <div class="hero-title">{current["hero_title"]}</div>
                    <p class="hero-summary">{current["hero_summary"]}</p>

                    <div class="hero-stack">
                        {stack_html}
                    </div>

                    <div class="hero-cta-row">
                        <a href="{PROFILE["linkedin"]}" target="_blank" class="cta-btn cta-primary">{buttons["linkedin"]}</a>
                        <a href="{PROFILE["github"]}" target="_blank" class="cta-btn cta-secondary">{buttons["github"]}</a>
                        <a href="{PROFILE["email"]}" class="cta-btn cta-secondary">{buttons["email"]}</a>
                    </div>
                </div>

                <div class="hero-panel">
                    <div>
                        <div class="hero-panel-label">{panel["label"]}</div>
                        <div class="hero-panel-value">{panel["value"]}</div>
                        <div class="hero-panel-text">{panel["text"]}</div>
                    </div>

                    <div class="hero-panel-grid">
                        {panel_cards_html}
                    </div>
                </div>
            </div>
        </div>
        """
    )
    render_highlights()


def render_home_page():
    section_renderers = [
        ("home", render_hero),
        ("about", render_about),
        ("skills", render_skills),
        ("projects", render_projects),
        ("method", render_method),
        ("experience", render_experience),
        ("contact", render_contact),
    ]

    for section_key, render_fn in section_renderers:
        with st.container(key=f"page_{section_key}"):
            render_html(f'<div id="{section_key}" class="section-anchor"></div>')
            if section_key == "home":
                render_language_switcher()
            render_fn()


def render_highlights():
    current = content()
    cols = st.columns(len(current["metrics"]))
    for col, (number, label) in zip(cols, current["metrics"]):
        with col:
            render_html(
                f"""
                <div class="metric-box">
                    <div class="metric-number">{number}</div>
                    <div class="metric-label">{label}</div>
                </div>
                """
            )


def render_about():
    current = content()["about"]

    render_section_header(
        current["eyebrow"],
        current["title"],
        current["subtitle"],
    )

    col1, col2 = st.columns([3, 2], gap="large")

    with col1:
        paragraphs_html = "".join(
            f'<p style="color:#445168; line-height:1.85; font-size:0.97rem; margin-top:{0 if i == 0 else 14}px;">{text}</p>'
            for i, text in enumerate(current["paragraphs"])
        )
        render_html(
            f"""
            <div class="card">
                {paragraphs_html}
            </div>
            """
        )

    with col2:
        for area in current["areas"]:
            render_html(
                f"""
                <div class="card card-accent" style="margin-bottom:12px;">
                    <div style="font-size:1.2rem; margin-bottom:6px;">{area["icon"]}</div>
                    <div style="font-weight:700; color:#111111; font-size:0.92rem; margin-bottom:4px;">
                        {area["title"]}
                    </div>
                    <div style="color:#6b7790; font-size:0.82rem; line-height:1.6;">
                        {area["desc"]}
                    </div>
                </div>
                """
            )


def render_skills():
    current = content()["skills"]

    render_section_header(
        current["eyebrow"],
        current["title"],
        current["subtitle"],
    )

    flow_parts = []

    for idx, skill_group in enumerate(current["groups"], start=1):
        tags_html = "".join(
            f'<span class="skills-tag">{tool}</span>'
            for tool in skill_group["tools"]
        )

        flow_parts.append(
            f"""
            <div class="skills-node">
                <div class="skills-node-header">
                    <div class="skills-node-title">{skill_group["title"]}</div>
                    <div class="skills-node-icon">{skill_group["icon"]}</div>
                </div>
                <div class="skills-tags-wrap">
                    {tags_html}
                </div>
            </div>
            """
        )

        if idx < len(current["groups"]):
            flow_parts.append('<div class="skills-connector" aria-hidden="true"></div>')

    render_html(
        f"""
        <div class="skills-shell">
            <div class="skills-flow">
                {''.join(flow_parts)}
            </div>
        </div>
        <div class="skills-note">{current["note"]}</div>
        """
    )


def render_projects():
    current = content()["projects"]
    buttons = content()["buttons"]

    render_section_header(
        current["eyebrow"],
        current["title"],
        current["subtitle"],
    )

    cards_html = []
    for project in current["items"]:
        cards_html.append(
            f"""
            <div class="project-card">
                <div class="project-card-head">
                    <div class="project-card-emoji">{project["emoji"]}</div>
                    <div class="project-card-title">{project["title"]}</div>
                </div>

                <div class="project-block">
                    <div class="project-kicker">{current["problem"]}</div>
                    <div class="project-copy">{project["problem"]}</div>
                </div>

                <div class="project-block">
                    <div class="project-kicker">{current["insights"]}</div>
                    <div class="project-copy">{project["insights"]}</div>
                </div>

                <div class="project-block">
                    <div class="project-kicker">{current["impact"]}</div>
                    <div class="project-copy">{project["impact"]}</div>
                </div>

                <div class="project-footer">
                    <div>{render_tags(project["tools"])}</div>
                    <a href="{project["link"]}" target="_blank" class="project-link">{buttons["project"]}</a>
                </div>
            </div>
            """
        )

    render_html(
        f"""
        <div class="projects-showcase">
            {''.join(cards_html)}
        </div>
        """
    )


def render_method():
    current = content()["method"]

    render_section_header(
        current["eyebrow"],
        current["title"],
        current["subtitle"],
    )

    flow_parts = []

    for idx, (icon, label, desc) in enumerate(current["steps"], start=1):
        flow_parts.append(
            f"""
            <div class="method-node">
                <div class="method-node-header">
                    <div class="method-step-badge">{idx:02d}</div>
                    <div class="method-node-icon">{icon}</div>
                </div>
                <div class="method-node-title">{label}</div>
                <div class="method-node-desc">{desc}</div>
            </div>
            """
        )

        if idx < len(current["steps"]):
            flow_parts.append('<div class="method-connector" aria-hidden="true"></div>')

    render_html(
        f"""
        <div class="method-shell">
            <div class="method-flow">
                {''.join(flow_parts)}
            </div>
        </div>
        <div class="method-note">{current["note"]}</div>
        """
    )

    st.markdown("<br>", unsafe_allow_html=True)

    principles_html = "".join(
        f"""
        <div class="principle-mini-card">
            <div style="font-weight:700; font-size:0.88rem; color:#111111; margin-bottom:6px;">{title}</div>
            <div style="font-size:0.84rem; color:#6b7790; line-height:1.65;">{desc}</div>
        </div>
        """
        for title, desc in current["principles"]
    )

    render_html(
        f"""
        <div class="card" style="margin-top:8px;">
            <div style="font-family:'DM Serif Display',serif; font-size:1.1rem; color:#111111; margin-bottom:16px;">
                {current["principles_title"]}
            </div>
            <div class="principles-grid">
                {principles_html}
            </div>
        </div>
        """
    )


def render_experience():
    current = content()["experience"]
    total_items = len(current["items"])
    flow_parts = []

    render_section_header(
        current["eyebrow"],
        current["title"],
        current["subtitle"],
    )

    for idx, exp in enumerate(current["items"], start=1):
        meta = get_experience_meta(exp, idx, total_items)
        bullets_html = "".join(f"<li>{bullet}</li>" for bullet in exp["bullets"])

        flow_parts.append(
            f"""
            <div class="experience-item">
                <div class="experience-rail">
                    <div class="experience-node-wrap {'current' if meta['is_current'] else ''}">
                        <div class="experience-node {'current' if meta['is_current'] else ''}">
                            {meta['icon']}
                            <div class="experience-node-order">{idx:02d}</div>
                        </div>
                    </div>
                </div>

                <div class="experience-card-modern {'current' if meta['is_current'] else ''}">
                    <div class="experience-growth-bar"></div>

                    <div class="experience-card-top">
                        <div>
                            <div class="experience-company-modern">{exp["company"]}</div>
                            <div class="experience-role-modern">{exp["role"]}</div>

                            <div class="experience-badge-row">
                                <span class="experience-badge {'current' if meta['is_current'] else ''}">
                                    {meta['badge']}
                                </span>
                            </div>
                        </div>

                        <div class="experience-period-modern">{exp["period"]}</div>
                    </div>

                    <ul class="experience-list">
                        {bullets_html}
                    </ul>
                </div>
            </div>
            """
        )

    render_html(
        f"""
        <div class="experience-shell">
            <div class="experience-timeline">
                {''.join(flow_parts)}
            </div>
        </div>
        """
    )


def render_contact():
    current = content()["contact"]
    buttons = content()["buttons"]

    render_section_header(
        current["eyebrow"],
        current["title"],
        current["subtitle"],
    )

    col1, col2 = st.columns([2, 3], gap="large")

    with col1:
        render_html(
            f"""
            <div class="card" style="height:100%;">
                <p style="color:#445168; font-size:0.95rem; line-height:1.8; margin-bottom:20px;">
                    {current["intro_1"]}
                </p>
                <p style="color:#445168; font-size:0.95rem; line-height:1.8;">
                    {current["intro_2"]}
                </p>
            </div>
            """
        )

    with col2:
        for icon, platform, handle, link in current["items"]:
            render_html(
                f"""
                <a href="{link}" target="_blank" class="contact-item">
                    <span style="font-size:1.3rem;">{icon}</span>
                    <div>
                        <div style="font-size:0.7rem; text-transform:uppercase; letter-spacing:0.12em; color:#4b8dff; font-weight:700; margin-bottom:2px;">
                            {platform}
                        </div>
                        <div style="font-size:0.92rem; font-weight:600; color:#111111;">
                            {handle}
                        </div>
                    </div>
                </a>
                """
            )

    st.markdown("<br>", unsafe_allow_html=True)
    render_html(
        f"""
        <div style="text-align:center; padding:40px 20px; background:linear-gradient(135deg, #08111d 0%, #10213a 100%); border:1px solid rgba(106,154,255,0.14); border-radius:18px; margin-top:24px; box-shadow:0 18px 40px rgba(6,10,18,0.14);">
            <div style="font-family:'DM Serif Display',serif; font-size:1.8rem; color:#F7F9FF; margin-bottom:12px;">
                {current["cta_title"]}
            </div>
            <div style="color:#b6c6de; font-size:0.95rem; margin-bottom:24px;">
                {current["cta_text"]}
            </div>
            <a href="{PROFILE["email"]}"
               style="display:inline-block; background:linear-gradient(135deg, #86b8ff 0%, #4d8fff 100%); color:#07111d; padding:14px 36px; border-radius:10px; font-weight:700; font-size:0.9rem; text-decoration:none; letter-spacing:0.06em; box-shadow:0 10px 24px rgba(76,141,255,0.24);">
                {buttons["contact"]}
            </a>
        </div>
        """
    )

# ─────────────────────────────────────────────
# APP
# ─────────────────────────────────────────────
def main():
    init_session_state()
    inject_css()
    render_sidebar()
    render_home_page()

    render_html(
        f"""
        <div style="text-align:center; color:#7b89a1; font-size:0.76rem; padding-bottom:24px;">
            {content()["footer"]}
        </div>
        """
    )


if __name__ == "__main__":
    main()
