# Regime de Trabalho na Área de Dados: Preferências Entre Remoto, Híbrido e Presencial


**Luiz Felipe Assis Cavalcante, lfacavalcante@sga.pucminas.br**

**Arthur Viana Silva, arthur.silva.1564925@sga.pucminas.br**

**João Vitor de Lima, joao.lima.1594303@sga.pucminas.br**

**Márcio Douglas Cassemiro Junior, marcio.cassemiro@sga.pucminas.br**

**Gustavo Horta, gustavo.horta.1524459@sga.pucminas.br**


---

Professores:

** Prof. Hugo de Paula **
** Prof. Hayala Curto**

---

_Curso de Ciência de Dados, Unidade Praça da Liberdade_

_Instituto de Informática e Ciências Exatas – Pontifícia Universidade de Minas Gerais (PUC MINAS), Belo Horizonte – MG – Brasil_

---

_**Resumo**. Escrever aqui o resumo. O resumo deve contextualizar rapidamente o trabalho, descrever seu objetivo e, ao final, 
mostrar algum resultado relevante do trabalho (até 10 linhas)._

---

## 📑 Índice

- [Introdução](#introdução)
  - [Contextualização](#contextualização)
  - [Problema](#problema)
  - [Objetivo Geral](#objetivo-geral)
  - [Objetivos Específicos](#objetivos-específicos)
  - [Justificativas](#justificativas)
- [Público-alvo](#público-alvo)
- [Análise Exploratória dos Dados](#análise-exploratória-dos-dados)
  - [Dicionário de Dados](#dicionário-de-dados)
    - [`State_of_data_BR_2023_Kaggle - df_survey_2023`](#state_of_data_br_2023_kaggle---df_survey_2023)
    - [`PNAD_Roubos_Furtos_Brasil_2023`](#pnad_roubos_furtos_brasil_2023)
    - [`PNAD Média Horas Semanais de Trabalho Doméstico por Cor ou Raça - Brasil`](#pnad-média-horas-semanais-de-trabalho-doméstico-por-cor-ou-raça---brasil)
  - [`Análise Exploratória dos Dados - State_of_data_BR_2023_Kaggle`](#análise-exploratória-dos-dados---state_of_data_br_2023_kaggle---df_survey_2023)
  - [`Análise Exploratória dos Dados - PNAD Roubos e Furtos (Brasil)`](#análise-exploratória-dos-dados---pnad-roubos-e-furtos-brasil)


---


##	Introdução

A escolha do regime de trabalho — remoto, híbrido ou presencial — tem se tornado um tema central nas discussões sobre a dinâmica do mercado de trabalho, especialmente após a pandemia de Covid-19. Com a aceleração da adoção do trabalho remoto, muitos profissionais passaram a reconsiderar suas preferências quanto à flexibilidade e à forma como suas atividades são realizadas. No setor de dados, onde a tecnologia e a produtividade estão fortemente interligadas, a adaptação a novos modelos de trabalho gerou tanto benefícios quanto desafios.

Esse cenário levanta a questão sobre quais fatores determinam as escolhas dos profissionais de dados em relação ao regime de trabalho. A análise de aspectos como produtividade, tempo de deslocamento, saúde mental, flexibilidade e o impacto da interação social se torna essencial para entender as dinâmicas desse grupo específico. Compreender essas preferências pode não apenas ajudar a identificar as melhores práticas para aumentar a satisfação e a produtividade dos profissionais, mas também fornecer insights valiosos para empresas que buscam se adaptar às novas realidades do trabalho no pós-pandemia.

Este trabalho, portanto, tem como objetivo explorar os principais fatores que influenciam a escolha dos profissionais da área de dados quanto ao regime de trabalho. Dada a natureza altamente digital e analítica desse setor, compreender como elementos como produtividade, tempo de deslocamento, saúde mental, flexibilidade e interação social impactam suas preferências é essencial. A análise dessas variáveis pode fornecer insights valiosos tanto para profissionais que buscam otimizar seu desempenho e bem-estar quanto para empresas que precisam estruturar políticas de trabalho mais eficientes e alinhadas às demandas desse mercado específico.


###    Contextualização

A pandemia de Covid-19 acelerou mudanças na organização do trabalho, especialmente em áreas como tecnologia e dados, onde a digitalização permitiu uma rápida adaptação ao modelo remoto. Muitos profissionais do setor relataram ganhos em produtividade e qualidade de vida devido à flexibilidade e à eliminação do tempo de deslocamento, embora desafios como o isolamento social e a separação entre vida pessoal e profissional tenham surgido. Com a flexibilização das restrições, empresas adotaram diferentes regimes de trabalho, mas muitos profissionais de dados passaram a preferir o home office ou modelos híbridos.

###    Problema

O presente estudo busca ajudar empresas a compreender as prioridades de seus funcionários em relação ao regime de trabalho, com o objetivo de identificar os fatores que influenciam a escolha entre os modelos remoto, híbrido ou presencial. A pesquisa visa responder à seguinte pergunta orientada por dados: quais aspectos são determinantes para os profissionais na decisão de adotar um desses regimes de trabalho? Através dessa análise, espera-se fornecer insights valiosos para que as empresas possam ajustar suas políticas de trabalho de forma a atender melhor às necessidades e preferências de seus colaboradores.

> **Links Úteis**:
> - [Objetivos, Problema de pesquisa e Justificativa](https://medium.com/@versioparole/objetivos-problema-de-pesquisa-e-justificativa-c98c8233b9c3)


###    Objetivo geral

Desenvolver um sistema inteligente capaz de identificar padrões na escolha do regime de trabalho (remoto, híbrido ou presencial) e analisar os principais fatores que influenciam essa decisão. O sistema levará em consideração aspectos como mobilidade urbana, cargo, preferências dos profissionais e outras variáveis relevantes, gerando insights para empresas e formuladores de políticas trabalhistas.

####    Objetivos específicos

- Identificar os principais fatores que influenciam a escolha dos profissionais de dados pelo regime de trabalho remoto, híbrido ou presencial.  
- Analisar a variação das preferências por regime de trabalho de acordo com cargo, setor de atuação e localização.  
- Comparar os impactos da interação social e do tempo de deslocamento na decisão pelo modelo de trabalho adotado.  

> **Links Úteis**:
> - [Objetivo geral e objetivo específico: como fazer e quais verbos utilizar](https://blog.mettzer.com/diferenca-entre-objetivo-geral-e-objetivo-especifico/)

###    Justificativas

Este estudo se justifica pela necessidade de fornecer uma base analítica que auxilie empresas na formulação de cargos e na escolha do regime de trabalho mais adequado, considerando o perfil dos profissionais que possuem ou desejam atrair. Ao identificar os fatores que influenciam essa decisão, a pesquisa permite que organizações alinhem suas estratégias às expectativas do mercado, reduzindo a rotatividade e aumentando o engajamento dos colaboradores.

Além disso, compreender a relação entre fatores como cargo, setor de atuação, tempo de deslocamento e interação social pode ajudar empresas a ajustar suas políticas de trabalho para atender melhor às necessidades dos profissionais. Dessa forma, a pesquisa contribui para a construção de ambientes mais flexíveis e alinhados às novas dinâmicas do mercado pós-pandemia, beneficiando tanto as empresas quanto os trabalhadores.

> **Links Úteis**:
> - [Como montar a justificativa](https://guiadamonografia.com.br/como-montar-justificativa-do-tcc/)

##    Público alvo

O público-alvo desse sistema inclui empresas de diversos setores que desejam entender melhor as preferências de seus funcionários em relação ao regime de trabalho, auxiliando na formulação de políticas mais eficientes e atrativas. Além disso, gestores de Recursos Humanos podem utilizá-lo para otimizar modelos de trabalho e retenção de talentos. Pesquisadores e formuladores de políticas públicas também podem se beneficiar dos dados gerados para analisar impactos na mobilidade urbana, produtividade e qualidade de vida dos trabalhadores. Startups e consultorias especializadas em transformação digital e cultura organizacional podem usar os insights do sistema para oferecer soluções personalizadas a seus clientes.

> **Links Úteis**:
> - [Público-alvo](https://blog.hotmart.com/pt-br/publico-alvo/)
> - [Como definir o público alvo](https://exame.com/pme/5-dicas-essenciais-para-definir-o-publico-alvo-do-seu-negocio/)
> - [Público-alvo: o que é, tipos, como definir seu público e exemplos](https://klickpages.com.br/blog/publico-alvo-o-que-e/)
> - [Qual a diferença entre público-alvo e persona?](https://rockcontent.com/blog/diferenca-publico-alvo-e-persona/)

## Análise exploratórida dos dados

###    Dicionário de dados
 
#### `State_of_data_BR_2023_Kaggle - df_survey_2023`
Essa base de dados contém os dados relacionados aos profissionais de dados que serão utilizados como base para o atual estudo

Os atributos que compõem o dataset são:

<details>
	<summary>📌Clique para ver todos os atributos⬇️</summary>
	
| Atributo | Tipo |
|----------|------|
| ('P0', 'id') | Quantitativo Discreto |
| ('P1_a ', 'Idade') | Quantitativo Contínuo |
| ('P1_a_1 ', 'Faixa idade') | Categórico Polinomial Não Ordinal |
| ('P1_b ', 'Genero') | Categórico Polinomial Não Ordinal |
| ('P1_c ', 'Cor/raca/etnia') | Categórico Polinomial Não Ordinal |
| ('P1_d ', 'PCD') | Categórico Binário |
| ('P1_e ', 'experiencia_profissional_prejudicada') | Categórico Polinomial Não Ordinal |
| ('P1_e_1 ', 'Não acredito que minha experiência profissional seja afetada') | Categórico Binário |
| ('P1_e_2 ', 'Experiencia prejudicada devido a minha Cor Raça Etnia') | Categórico Binário |
| ('P1_e_3 ', 'Experiencia prejudicada devido a minha identidade de gênero') | Categórico Binário |
| ('P1_e_4 ', 'Experiencia prejudicada devido ao fato de ser PCD') | Categórico Binário |
| ('P1_f ', 'aspectos_prejudicados') | Categórico Polinomial Não Ordinal |
| ('P1_f_1', 'Quantidade de oportunidades de emprego/vagas recebidas') | Categórico Binário |
| ('P1_f_2', 'Senioridade das vagas recebidas em relação à sua experiência') | Categórico Binário |
| ('P1_f_3', 'Aprovação em processos seletivos/entrevistas') | Categórico Binário |
| ('P1_f_4', 'Oportunidades de progressão de carreira') | Categórico Binário |
| ('P1_f_5', 'Velocidade de progressão de carreira') | Categórico Binário |
| ('P1_f_6', 'Nível de cobrança no trabalho/Stress no trabalho') | Categórico Binário |
| ('P1_f_7', 'Atenção dada diante das minhas opiniões e ideias') | Categórico Binário |
| ('P1_f_8', 'Relação com outros membros da empresa, em momentos de trabalho') | Categórico Binário |
| ('P1_f_9', 'Relação com outros membros da empresa, em momentos de integração e outros momentos fora do trabalho') | Categórico Binário |
| ('P1_g ', 'vive_no_brasil') | Categórico Binário |
| ('P1_i ', 'Estado onde mora') | Categórico Polinomial Não Ordinal |
| ('P1_i_1 ', 'uf onde mora') | Categórico Polinomial Não Ordinal |
| ('P1_i_2 ', 'Regiao onde mora') | Categórico Polinomial Não Ordinal |
| ('P1_j ', 'Mudou de Estado?') | Categórico Binário |
| ('P1_k ', 'Regiao de origem') | Categórico Polinomial Não Ordinal |
| ('P1_l ', 'Nivel de Ensino') | Categórico Polinomial Não Ordinal |
| ('P1_m ', 'Área de Formação') | Categórico Polinomial Não Ordinal |
| ('P2_a ', 'Qual sua situação atual de trabalho?') | Categórico Polinomial Não Ordinal |
| ('P2_b ', 'Setor') | Categórico Polinomial Não Ordinal |
| ('P2_c ', 'Numero de Funcionarios') | Categórico Polinomial Não Ordinal |
| ('P2_d ', 'Gestor?') | Categórico Binário |
| ('P2_e ', 'Cargo como Gestor') | Categórico Polinomial Não Ordinal |
| ('P2_f ', 'Cargo Atual') | Categórico Polinomial Não Ordinal |
| ('P2_g ', 'Nivel') | Categórico Polinomial Ordinal |
| ('P2_h ', 'Faixa salarial') | Categórico Polinomial Ordinal |
| ('P2_i ', 'Quanto tempo de experiência na área de dados você tem?') | Categórico Polinomial Ordinal |
| ('P2_j ', 'Quanto tempo de experiência na área de TI/Engenharia de Software você teve antes de começar a trabalhar na área de dados?') | Categórico Polinomial Ordinal |
| ('P2_k ', 'Você está satisfeito na sua empresa atual?') | Categórico Binário |
| ('P2_l ', 'Qual o principal motivo da sua insatisfação com a empresa atual?') | Categórico Polinomial Não Ordinal |
| ('P2_l_1 ', 'Falta de oportunidade de crescimento no emprego atual') | Categórico Binário |
| ('P2_l_2 ', 'Salário atual não corresponde ao mercado') | Categórico Binário |
| ('P2_l_3 ', 'Não tenho uma boa relação com meu líder/gestor') | Categórico Binário |
| ('P2_l_4 ', 'Gostaria de trabalhar em em outra área de atuação') | Categórico Binário |
| ('P2_l_5 ', 'Gostaria de receber mais benefícios') | Categórico Binário |
| ('P2_l_6 ', 'O clima de trabalho/ambiente não é bom') | Categórico Binário |
| ('P2_l_7 ', 'Falta de maturidade analítica na empresa') | Categórico Binário |
| ('P2_m ', 'Você participou de entrevistas de emprego nos últimos 6 meses?') | Categórico Polinomial Não Ordinal |
| ('P2_n ', 'Você pretende mudar de emprego nos próximos 6 meses?') | Categórico Polinomial Não Ordinal |
| ('P2_o ', 'Quais os principais critérios que você leva em consideração no momento de decidir onde trabalhar?') | Categórico Polinomial Não Ordinal |
| ('P2_o_1 ', 'Remuneração/Salário') | Categórico Binário |
| ('P2_o_2 ', 'Benefícios') | Categórico Binário |
| ('P2_o_3 ', 'Propósito do trabalho e da empresa') | Categórico Binário |
| ('P2_o_4 ', 'Flexibilidade de trabalho remoto') | Categórico Binário |
| ('P2_o_5 ', 'Ambiente e clima de trabalho') | Categórico Binário |
| ('P2_o_6 ', 'Oportunidade de aprendizado e trabalhar com referências na área') | Categórico Binário |
| ('P2_o_7 ', 'Plano de carreira e oportunidades de crescimento profissional') | Categórico Binário |
| ('P2_o_8 ', 'Maturidade da empresa em termos de tecnologia e dados') | Categórico Binário |
| ('P2_o_9 ', 'Qualidade dos gestores e líderes') | Categórico Binário |
| ('P2_o_10 ', 'Reputação que a empresa tem no mercado') | Categórico Binário |
| ('P2_q ', 'Empresa que trabaha passou por layoff em 2023') | Categórico Polinomial Não Ordinal |
| ('P2_r ', 'Atualmente qual a sua forma de trabalho?') | Categórico Polinomial Não Ordinal |
| ('P2_s ', 'Qual a forma de trabalho ideal para você?') | Categórico Polinomial Não Ordinal |
| ('P2_t ', 'Caso sua empresa decida pelo modelo 100% presencial qual será sua atitude?') | Categórico Polinomial Não Ordinal |
| ('P3_a ', 'Qual o número aproximado de pessoas que atuam com dados na sua empresa hoje?') | Categórico Polinomial Não Ordinal |
| ('P3_b ', 'Quais desses papéis/cargos fazem parte do time (ou chapter) de dados da sua empresa?') | Categórico Polinomial Não Ordinal |
| ('P3_b_1 ', 'Analytics Engineer') | Categórico Binário |
| ('P3_b_2 ', 'Engenharia de Dados/Data Engineer') | Categórico Binário |
| ('P3_b_3 ', 'Analista de Dados/Data Analyst') | Categórico Binário |
| ('P3_b_4 ', 'Cientista de Dados/Data Scientist') | Categórico Binário |
| ('P3_b_5 ', 'Database Administrator/DBA') | Categórico Binário |
| ('P3_b_6 ', 'Analista de Business Intelligence/BI') | Categórico Binário |
| ('P3_b_7 ', 'Arquiteto de Dados/Data Architect') | Categórico Binário |
| ('P3_b_8 ', 'Data Product Manager/DPM') | Categórico Binário |
| ('P3_b_9 ', 'Business Analyst') | Categórico Binário |
| ('P3_c ', 'Quais dessas responsabilidades fazem parte da sua rotina atual de trabalho como gestor?') | Categórico Polinomial Não Ordinal |
| ('P3_c_1 ', 'Pensar na visão de longo prazo de dados da empresa e fortalecimento da cultura analítica da companhia.') | Categórico Binário |
| ('P3_c_2 ', 'Organização de treinamentos e iniciativas com o objetivo de aumentar a maturidade analítica das áreas de negócios.') | Categórico Binário |
| ('P3_c_3 ', 'Atração, seleção e contratação de talentos para o time de dados.') | Categórico Binário |
| ('P3_c_4 ', 'Decisão sobre contratação de ferramentas e tecnologias relacionadas a dados.') | Categórico Binário |
| ('P3_c_5 ', 'Sou gestor da equipe responsável pela engenharia de dados e por manter o Data Lake da empresa como fonte única dos dados, garantindo a qualidade e confiabilidade da informação.') | Categórico Binário |
| ('P3_c_6 ', 'Sou gestor da equipe responsável pela entrega de dados, estudos, relatórios e dashboards para as áreas de negócio da empresa.') | Categórico Binário |
| ('P3_c_7 ', 'Sou gestor da equipe responsável por iniciativas e projetos envolvendo Inteligência Artificial e Machine Learning.') | Categórico Binário |
| ('P3_c_8 ', 'Apesar de ser gestor ainda atuo na parte técnica, construindo soluções/análises/modelos etc.') | Categórico Binário |
| ('P3_c_9 ', 'Gestão de projetos de dados, cuidando das etapas, equipes envolvidas, atingimento dos objetivos etc.') | Categórico Binário |
| ('P3_c_10 ', 'Gestão de produtos de dados, cuidando da visão dos produtos, backlog, feedback de usuários etc.') | Categórico Binário |
| ('P3_c_11 ', 'Gestão de pessoas, apoio no desenvolvimento das pessoas, evolução de carreira') | Categórico Binário |
| ('P3_d ', 'Quais são os 3 maiores desafios que você tem como gestor no atual momento?') | Categórico Polinomial Não Ordinal |
| ('P3_d_1 ', 'a Contratar novos talentos.') | Categórico Binário |
| ('P3_d_2 ', 'b Reter talentos.') | Categórico Binário |
| ('P3_d_3 ', 'c Convencer a empresa a aumentar os investimentos na área de dados.') | Categórico Binário |
| ('P3_d_4 ', 'd Gestão de equipes no ambiente remoto.') | Categórico Binário |
| ('P3_d_5 ', 'e Gestão de projetos envolvendo áreas multidisciplinares da empresa.') | Categórico Binário |
| ('P3_d_6 ', 'f Organizar as informações e garantir a qualidade e confiabilidade.') | Categórico Binário |
| ('P3_d_7 ', 'g Conseguir processar e armazenar um alto volume de dados.') | Categórico Binário |
| ('P3_d_8 ', 'h Conseguir gerar valor para as áreas de negócios através de estudos e experimentos.') | Categórico Binário |
| ('P3_d_9 ', 'i Desenvolver e manter modelos Machine Learning em produção.') | Categórico Binário |
| ('P3_d_10 ', 'j Gerenciar a expectativa das áreas de negócio em relação as entregas das equipes de dados.') | Categórico Binário |
| ('P3_d_11 ', 'k Garantir a manutenção dos projetos e modelos em produção, em meio ao crescimento da empresa.') | Categórico Binário |
| ('P3_d_12 ', 'Conseguir levar inovação para a empresa através dos dados.') | Categórico Binário |
| ('P3_d_13 ', 'Garantir retorno do investimento (ROI) em projetos de dados.') | Categórico Binário |
| ('P3_d_14 ', 'Dividir o tempo entre entregas técnicas e gestão.') | Categórico Binário |
| ('P3_e ', 'AI Generativa é uma prioridade em sua empresa?') | Categórico Polinomial Não Ordinal |
| ('P3_f ', 'Tipos de uso de AI Generativa e LLMs na empresa') | Categórico Polinomial Não Ordinal |
| ('P3_f_1 ', 'Colaboradores usando AI generativa de forma independente e descentralizada') | Categórico Binário |
| ('P3_f_2 ', 'Direcionamento centralizado do uso de AI generativa') | Categórico Binário |
| ('P3_f_3 ', 'Desenvolvedores utilizando Copilots') | Categórico Binário |
| ('P3_f_4 ', 'AI Generativa e LLMs para melhorar produtos externos') | Categórico Binário |
| ('P3_f_5 ', 'AI Generativa e LLMs para melhorar produtos internos para os colaboradores') | Categórico Binário |
| ('P3_f_6 ', 'IA Generativa e LLMs como principal frente do negócio') | Categórico Binário |
| ('P3_f_7 ', 'IA Generativa e LLMs não é prioridade') | Categórico Binário |
| ('P3_f_8 ', 'Não sei opinar sobre o uso de IA Generativa e LLMs na empresa') | Categórico Binário |
| ('P3_g ', 'Motivos que levam a empresa a não usar AI Genrativa e LLMs') | Categórico Polinomial Não Ordinal |
| ('P3_g_1 ', 'Falta de compreensão dos casos de uso') | Categórico Binário |
| ('P3_g_2 ', 'Falta de confiabilidade das saídas (alucinação dos modelos)') | Categórico Binário |
| ('P3_g_3 ', 'Incerteza em relação a regulamentação') | Categórico Binário |
| ('P3_g_4 ', 'Preocupações com segurança e privacidade de dados') | Categórico Binário |
| ('P3_g_5 ', 'Retorno sobre investimento (ROI) não comprovado de IA Generativa') | Categórico Binário |
| ('P3_g_6 ', 'Dados da empresa não estão prontos para uso de IA Generativa') | Categórico Binário |
| ('P3_g_7 ', 'Falta de expertise ou falta de recursos') | Categórico Binário |
| ('P3_g_8 ', 'Alta direção da empresa não vê valor ou não vê como prioridade') | Categórico Binário |
| ('P3_g_9 ', 'Preocupações com propriedade intelectual') | Categórico Binário |
| ('P4_a ', 'Mesmo que esse não seja seu cargo formal, você considera que sua atuação no dia a dia, reflete alguma das opções listadas abaixo?') | Categórico Polinomial Não Ordinal |
| ('P4_a_1 ', 'Atuacao') | Categórico Polinomial Não Ordinal |
| ('P4_b ', 'Quais das fontes de dados listadas você já analisou ou processou no trabalho?') | Categórico Polinomial Não Ordinal |
| ('P4_b_1 ', 'Dados relacionais (estruturados em bancos SQL)') | Categórico Binário |
| ('P4_b_2 ', 'Dados armazenados em bancos NoSQL') | Categórico Binário |
| ('P4_b_3 ', 'Imagens') | Categórico Binário |
| ('P4_b_4 ', 'Textos/Documentos') | Categórico Binário |
| ('P4_b_5 ', 'Vídeos') | Categórico Binário |
| ('P4_b_6 ', 'Áudios') | Categórico Binário |
| ('P4_b_7 ', 'Planilhas') | Categórico Binário |
| ('P4_b_8 ', 'Dados georeferenciados') | Categórico Binário |
| ('P4_c ', 'Entre as fontes de dados listadas, quais você utiliza na maior parte do tempo?') | Categórico Polinomial Não Ordinal |
| ('P4_c_1 ', 'Dados relacionais (estruturados em bancos SQL)') | Categórico Binário |
| ('P4_c_2 ', 'Dados armazenados em bancos NoSQL') | Categórico Binário |
| ('P4_c_3 ', 'Imagens') | Categórico Binário |
| ('P4_c_4 ', 'Textos/Documentos') | Categórico Binário |
| ('P4_c_5 ', 'Vídeos') | Categórico Binário |
| ('P4_c_6 ', 'Áudios') | Categórico Binário |
| ('P4_c_7 ', 'Planilhas') | Categórico Binário |
| ('P4_c_8 ', 'Dados georeferenciados') | Categórico Binário |
| ('P4_d ', 'Quais das linguagens listadas abaixo você utiliza no trabalho?') | Categórico Polinomial Não Ordinal |
| ('P4_d_1 ', 'SQL') | Categórico Binário |
| ('P4_d_2 ', 'R ') | Categórico Binário |
| ('P4_d_3 ', 'Python') | Categórico Binário |
| ('P4_d_4 ', 'C/C++/C#') | Categórico Binário |
| ('P4_d_5 ', '.NET') | Categórico Binário |
| ('P4_d_6 ', 'Java') | Categórico Binário |
| ('P4_d_7 ', 'Julia') | Categórico Binário |
| ('P4_d_8 ', 'SAS/Stata') | Categórico Binário |
| ('P4_d_9 ', 'Visual Basic/VBA') | Categórico Binário |
| ('P4_d_10 ', 'Scala') | Categórico Binário |
| ('P4_d_11 ', 'Matlab') | Categórico Binário |
| ('P4_d_12 ', 'Rust') | Categórico Binário |
| ('P4_d_13 ', 'PHP') | Categórico Binário |
| ('P4_d_14 ', 'JavaScript') | Categórico Binário |
| ('P4_d_15 ', 'Não utilizo nenhuma linguagem') | Categórico Binário |
| ('P4_e ', 'Entre as linguagens listadas abaixo, qual é a que você mais utiliza no trabalho?') | Categórico Polinomial Não Ordinal |
| ('P4_f ', 'Entre as linguagens listadas abaixo, qual é a sua preferida?') | Categórico Polinomial Não Ordinal |
| ('P4_g ', 'Quais dos bancos de dados/fontes de dados listados abaixo você utiliza no trabalho?') | Categórico Polinomial Não Ordinal |
| ('P4_g_1 ', 'MySQL') | Categórico Binário |
| ('P4_g_2 ', 'Oracle') | Categórico Binário |
| ('P4_g_3 ', 'SQL SERVER') | Categórico Binário |
| ('P4_g_4 ', 'Amazon Aurora ou RDS') | Categórico Binário |
| ('P4_g_5 ', 'DynamoDB') | Categórico Binário |
| ('P4_g_6 ', 'CoachDB') | Categórico Binário |
| ('P4_g_7 ', 'Cassandra') | Categórico Binário |
| ('P4_g_8 ', 'MongoDB') | Categórico Binário |
| ('P4_g_9 ', 'MariaDB') | Categórico Binário |
| ('P4_g_10 ', 'Datomic') | Categórico Binário |
| ('P4_g_11 ', 'S3') | Categórico Binário |
| ('P4_g_12 ', 'PostgreSQL') | Categórico Binário |
| ('P4_g_13 ', 'ElasticSearch') | Categórico Binário |
| ('P4_g_14 ', 'DB2') | Categórico Binário |
| ('P4_g_15 ', 'Microsoft Access') | Categórico Binário |
| ('P4_g_16 ', 'SQLite') | Categórico Binário |
| ('P4_g_17 ', 'Sybase') | Categórico Binário |
| ('P4_g_18 ', 'Firebase') | Categórico Binário |
| ('P4_g_19 ', 'Vertica') | Categórico Binário |
| ('P4_g_20 ', 'Redis') | Categórico Binário |
| ('P4_g_21 ', 'Neo4J') | Categórico Binário |
| ('P4_g_22 ', 'Google BigQuery') | Categórico Binário |
| ('P4_g_23 ', 'Google Firestore') | Categórico Binário |
| ('P4_g_24 ', 'Amazon Redshift') | Categórico Binário |
| ('P4_g_25 ', 'Amazon Athena') | Categórico Binário |
| ('P4_g_26 ', 'Snowflake') | Categórico Binário |
| ('P4_g_27 ', 'Databricks') | Categórico Binário |
| ('P4_g_28 ', 'HBase') | Categórico Binário |
| ('P4_g_29 ', 'Presto') | Categórico Binário |
| ('P4_g_30 ', 'Splunk') | Categórico Binário |
| ('P4_g_31 ', 'SAP HANA') | Categórico Binário |
| ('P4_g_32 ', 'Hive') | Categórico Binário |
| ('P4_g_33 ', 'Firebird') | Categórico Binário |
| ('P4_h ', 'Dentre as opções listadas, qual sua Cloud preferida?') | Categórico Polinomial Não Ordinal |
| ('P4_h_1 ', 'Azure (Microsoft)') | Categórico Binário |
| ('P4_h_2 ', 'Amazon Web Services (AWS)') | Categórico Binário |
| ('P4_h_3 ', 'Google Cloud (GCP)') | Categórico Binário |
| ('P4_h_4 ', 'Oracle Cloud') | Categórico Binário |
| ('P4_h_5 ', 'IBM') | Categórico Binário |
| ('P4_h_6 ', 'Servidores On Premise/Não utilizamos Cloud') | Categórico Binário |
| ('P4_h_7 ', 'Cloud Própria') | Categórico Binário |
| ('P4_i ', 'Cloud preferida') | Categórico Polinomial Não Ordinal |
| ('P4_j ', 'Ferramenta de BI utilizada no dia a dia') | Categórico Polinomial Não Ordinal |
| ('P4_j_1 ', 'Microsoft PowerBI') | Categórico Binário |
| ('P4_j_2 ', 'Qlik View/Qlik Sense') | Categórico Binário |
| ('P4_j_3 ', 'Tableau') | Categórico Binário |
| ('P4_j_4 ', 'Metabase') | Categórico Binário |
| ('P4_j_5 ', 'Superset') | Categórico Binário |
| ('P4_j_6 ', 'Redash') | Categórico Binário |
| ('P4_j_7 ', 'Looker') | Categórico Binário |
| ('P4_j_8 ', 'Looker Studio(Google Data Studio)') | Categórico Binário |
| ('P4_j_9 ', 'Amazon Quicksight') | Categórico Binário |
| ('P4_j_10 ', 'Mode') | Categórico Binário |
| ('P4_j_11 ', 'Alteryx') | Categórico Binário |
| ('P4_j_12 ', 'MicroStrategy') | Categórico Binário |
| ('P4_j_13 ', 'IBM Analytics/Cognos') | Categórico Binário |
| ('P4_j_14 ', 'SAP Business Objects/SAP Analytics') | Categórico Binário |
| ('P4_j_15 ', 'Oracle Business Intelligence') | Categórico Binário |
| ('P4_j_16 ', 'Salesforce/Einstein Analytics') | Categórico Binário |
| ('P4_j_17 ', 'Birst') | Categórico Binário |
| ('P4_j_18 ', 'SAS Visual Analytics') | Categórico Binário |
| ('P4_j_19 ', 'Grafana') | Categórico Binário |
| ('P4_j_20 ', 'TIBCO Spotfire') | Categórico Binário |
| ('P4_j_21 ', 'Pentaho') | Categórico Binário |
| ('P4_j_22 ', 'Fazemos todas as análises utilizando apenas Excel ou planilhas do google') | Categórico Binário |
| ('P4_j_23 ', 'Não utilizo nenhuma ferramenta de BI no trabalho') | Categórico Binário |
| ('P4_k ', 'Qual sua ferramenta de BI preferida?') | Categórico Polinomial Não Ordinal |
| ('P4_l ', 'Qual o tipo de uso de AI Generativa e LLMs na empresa') | Categórico Polinomial Não Ordinal |
| ('P4_l_1 ', 'Colaboradores usando AI generativa de forma independente e descentralizada') | Categórico Binário |
| ('P4_l_2 ', 'Direcionamento centralizado do uso de AI generativa') | Categórico Binário |
| ('P4_l_3 ', 'Desenvolvedores utilizando Copilots') | Categórico Binário |
| ('P4_l_4 ', 'AI Generativa e LLMs para melhorar produtos externos para os clientes finais') | Categórico Binário |
| ('P4_l_5 ', 'AI Generativa e LLMs para melhorar produtos internos para os colaboradores') | Categórico Binário |
| ('P4_l_6 ', 'IA Generativa e LLMs como principal frente do negócio') | Categórico Binário |
| ('P4_l_7 ', 'IA Generativa e LLMs não é prioridade') | Categórico Binário |
| ('P4_l_8 ', 'Não sei opinar sobre o uso de IA Generativa e LLMs na empresa') | Categórico Binário |
| ('P4_m ', 'Utiliza ChatGPT ou LLMs no trabalho?') | Categórico Polinomial Não Ordinal |
| ('P4_m_1 ', 'Não uso soluções de AI Generativa com foco em produtividade') | Categórico Binário |
| ('P4_m_2 ', 'Uso soluções gratuitas de AI Generativa com foco em produtividade') | Categórico Binário |
| ('P4_m_3 ', 'Uso e pago pelas soluções de AI Generativa com foco em produtividade') | Categórico Binário |
| ('P4_m_4 ', 'A empresa que trabalho paga pelas soluções de AI Generativa com foco em produtividade') | Categórico Binário |
| ('P4_m_5 ', 'Uso soluções do tipo Copilot') | Categórico Binário |
| ('P5_a ', 'Qual seu objetivo na área de dados?') | Categórico Polinomial Não Ordinal |
| ('P5_b ', 'Qual oportunidade você está buscando?') | Categórico Polinomial Não Ordinal |
| ('P5_c ', 'Há quanto tempo você busca uma oportunidade na área de dados?') | Categórico Polinomial Não Ordinal |
| ('P5_d ', 'Como tem sido a busca por um emprego na área de dados?') | Categórico Polinomial Não Ordinal |
| ('P6_a ', 'Quais das opções abaixo fazem parte da sua rotina no trabalho atual como engenheiro de dados?') | Categórico Polinomial Não Ordinal |
| ('P6_a_1 ', 'Desenvolvo pipelines de dados utilizando linguagens de programação como Python, Scala, Java etc.') | Categórico Binário |
| ('P6_a_2 ', 'Realizo construções de ETL's em ferramentas como Pentaho, Talend, Dataflow etc.') | Categórico Binário |
| ('P6_a_3 ', 'Crio consultas através da linguagem SQL para exportar informações e compartilhar com as áreas de negócio.') | Categórico Binário |
| ('P6_a_4 ', 'Atuo na integração de diferentes fontes de dados através de plataformas proprietárias como Stitch Data, Fivetran etc.') | Categórico Binário |
| ('P6_a_5 ', 'Modelo soluções de arquitetura de dados, criando componentes de ingestão de dados, transformação e recuperação da informação.') | Categórico Binário |
| ('P6_a_6 ', 'Desenvolvo/cuido da manutenção de repositórios de dados baseados em streaming de eventos como Data Lakes e Data Lakehouses.') | Categórico Binário |
| ('P6_a_7 ', 'Atuo na modelagem dos dados, com o objetivo de criar conjuntos de dados como Data Warehouses, Data Marts etc.') | Categórico Binário |
| ('P6_a_8 ', 'Cuido da qualidade dos dados, metadados e dicionário de dados.') | Categórico Binário |
| ('P6_a_9 ', 'Nenhuma das opções listadas refletem meu dia a dia.') | Categórico Binário |
| ('P6_b ', 'Quais as ferramentas/tecnologias de ETL que você utiliza no trabalho como Data Engineer?') | Categórico Polinomial Não Ordinal |
| ('P6_b_1 ', 'Scripts Python') | Categórico Binário |
| ('P6_b_2 ', 'SQL & Stored Procedures') | Categórico Binário |
| ('P6_b_3 ', 'Apache Airflow') | Categórico Binário |
| ('P6_b_4 ', 'Apache NiFi') | Categórico Binário |
| ('P6_b_5 ', 'Luigi') | Categórico Binário |
| ('P6_b_6 ', 'AWS Glue') | Categórico Binário |
| ('P6_b_7 ', 'Talend') | Categórico Binário |
| ('P6_b_8 ', 'Pentaho') | Categórico Binário |
| ('P6_b_9 ', 'Alteryx') | Categórico Binário |
| ('P6_b_10 ', 'Stitch') | Categórico Binário |
| ('P6_b_11 ', 'Fivetran') | Categórico Binário |
| ('P6_b_12 ', 'Google Dataflow') | Categórico Binário |
| ('P6_b_13 ', 'Oracle Data Integrator') | Categórico Binário |
| ('P6_b_14 ', 'IBM DataStage') | Categórico Binário |
| ('P6_b_15 ', 'SAP BW ETL') | Categórico Binário |
| ('P6_b_16 ', 'SQL Server Integration Services (SSIS)) | Categórico Binário |
| ('P6_b_17 ', 'SAS Data Integration') | Categórico Binário |
| ('P6_b_18 ', 'Qlik Sense') | Categórico Binário |
| ('P6_b_19 ', 'Knime') | Categórico Binário |
| ('P6_b_20 ', 'Databricks') | Categórico Binário |
| ('P6_b_21 ', 'Não utilizo ferramentas de ETL') | Categórico Binário |
| ('P6_c ', 'Sua organização possui um Data Lake?') | Categórico Binário |
| ('P6_d ', 'Qual tecnologia utilizada como plataforma do Data Lake?') | Categórico Polinomial Não Ordinal |
| ('P6_e ', 'Sua organização possui um Data Warehouse?') | Categórico Binário |
| ('P6_f ', 'Qual tecnologia utilizada como plataforma do Data Warehouse?') | Categórico Polinomial Não Ordinal |
| ('P6_g ', 'Quais as ferramentas de gestão de Qualidade de dados, Metadados e catálogo de dados você utiliza no trabalho?') | Categórico Polinomial Não Ordinal |
| ('P6_h ', 'Em qual das opções abaixo você gasta a maior parte do seu tempo?') | Categórico Polinomial Não Ordinal |
| ('P6_h_1 ', 'Desenvolvendo pipelines de dados utilizando linguagens de programação como Python, Scala, Java etc.') | Categórico Binário |
| ('P6_h_2 ', 'Realizando construções de ETL's em ferramentas como Pentaho, Talend, Dataflow etc.') | Categórico Binário |
| ('P6_h_3 ', 'Criando consultas através da linguagem SQL para exportar informações e compartilhar com as áreas de negócio.') | Categórico Binário |
| ('P6_h_4 ', 'Atuando na integração de diferentes fontes de dados através de plataformas proprietárias como Stitch Data, Fivetran etc.') | Categórico Binário |
| ('P6_h_5 ', 'Modelando soluções de arquitetura de dados, criando componentes de ingestão de dados, transformação e recuperação da informação.') | Categórico Binário |
| ('P6_h_6 ', 'Desenvolvendo/cuidando da manutenção de repositórios de dados baseados em streaming de eventos como Data Lakes e Data Lakehouses.') | Categórico Binário |
| ('P6_h_7 ', 'Atuando na modelagem dos dados, com o objetivo de criar conjuntos de dados como Data Warehouses, Data Marts etc.') | Categórico Binário |
| ('P6_h_8 ', 'Cuidando da qualidade dos dados, metadados e dicionário de dados.') | Categórico Binário |
| ('P6_h_9 ', 'Nenhuma das opções listadas refletem meu dia a dia.') | Categórico Binário |
| ('P7_1 ', 'Quais das opções abaixo fazem parte da sua rotina no trabalho atual com análise de dados?') | Categórico Polinomial Não Ordinal |
| ('P7_a_1 ', 'Processo e analiso dados utilizando linguagens de programação como Python, R etc.') | Categórico Binário |
| ('P7_a_2 ', 'Realizo construções de dashboards em ferramentas de BI como PowerBI, Tableau, Looker, Qlik etc.') | Categórico Binário |
| ('P7_a_3 ', 'Crio consultas através da linguagem SQL para exportar informações e compartilhar com as áreas de negócio.') | Categórico Binário |
| ('P7_a_4 ', 'Utilizo API's para extrair dados e complementar minhas análises.') | Categórico Binário |
| ('P7_a_5 ', 'Realizo experimentos e estudos utilizando metodologias estatísticas como teste de hipótese, modelos de regressão etc.') | Categórico Binário |
| ('P7_a_6 ', 'Desenvolvo/cuido da manutenção de ETL's utilizando tecnologias como Talend, Pentaho, Airflow, Dataflow etc.') | Categórico Binário |
| ('P7_a_7 ', 'Atuo na modelagem dos dados, com o objetivo de criar conjuntos de dados, Data Warehouses, Data Marts etc.') | Categórico Binário |
| ('P7_a_8 ', 'Desenvolvo/cuido da manutenção de planilhas para atender as áreas de negócio.') | Categórico Binário |
| ('P7_a_9 ', 'Utilizo ferramentas avançadas de estatística como SASS, PSS, Stata etc') | Categórico Binário |
| ('P7_a_10 ', 'Nenhuma das opções listadas refletem meu dia a dia.') | Categórico Binário |
| ('P7_b ', 'Quais as ferramentas/tecnologias de ETL que você utiliza no trabalho como Data Analyst?') | Categórico Polinomial Não Ordinal |
| ('P7_b_1 ', 'Scripts Python') | Categórico Binário |
| ('P7_b_2 ', 'SQL & Stored Procedures') | Categórico Binário |
| ('P7_b_3 ', 'Apache Airflow') | Categórico Binário |
| ('P7_b_4 ', 'Apache NiFi') | Categórico Binário |
| ('P7_b_5 ', 'Luigi') | Categórico Binário |
| ('P7_b_6 ', 'AWS Glue') | Categórico Binário |
| ('P7_b_7 ', 'Talend') | Categórico Binário |
| ('P7_b_8 ', 'Pentaho') | Categórico Binário |
| ('P7_b_9 ', 'Alteryx') | Categórico Binário |
| ('P7_b_10 ', 'Stitch') | Categórico Binário |
| ('P7_b_11 ', 'Fivetran') | Categórico Binário |
| ('P7_b_12 ', 'Google Dataflow') | Categórico Binário |
| ('P7_b_13 ', 'Oracle Data Integrator') | Categórico Binário |
| ('P7_b_14 ', 'IBM DataStage') | Categórico Binário |
| ('P7_b_15 ', 'SAP BW ETL') | Categórico Binário |
| ('P7_b_16 ', 'SQL Server Integration Services (SSIS)') | Categórico Binário |
| ('P7_b_17 ', 'SAS Data Integration') | Categórico Binário |
| ('P7_b_18 ', 'Qlik Sense') | Categórico Binário |
| ('P7_b_19 ', 'Knime') | Categórico Binário |
| ('P7_b_20 ', 'Databricks') | Categórico Binário |
| ('P7_b_21 ', 'Não utilizo ferramentas de ETL') | Categórico Binário |
| ('P7_c ', 'Sua empresa utiliza alguma das ferramentas listadas para dar mais autonomia em análise de dados para as áreas de negócio?') | Categórico Polinomial Não Ordinal |
| ('P7_c_1 ', 'Ferramentas de AutoML como H2O.ai, Data Robot, BigML etc.') | Categórico Binário |
| ('P7_c_2 ', '""Point and Click"" Analytics como Alteryx, Knime, Rapidminer etc.') | Categórico Binário |
| ('P7_c_3 ', 'Product metricts & Insights como Mixpanel, Amplitude, Adobe Analytics.') | Categórico Binário |
| ('P7_c_4 ', 'Ferramentas de análise dentro de ferramentas de CRM como Salesforce Einstein Anaytics ou Zendesk dashboards.') | Categórico Binário |
| ('P7_c_5 ', 'Minha empresa não utiliza essas ferramentas.') | Categórico Binário |
| ('P7_c_6 ', 'Não sei informar.') | Categórico Binário |
| ('P7_d ', 'Em qual das opções abaixo você gasta a maior parte do seu tempo de trabalho?') | Categórico Polinomial Não Ordinal |
| ('P7_d_1 ', 'Processando e analisando dados utilizando linguagens de programação como Python, R etc.') | Categórico Binário |
| ('P7_d_2 ', 'Realizando construções de dashboards em ferramentas de BI como PowerBI, Tableau, Looker, Qlik etc.') | Categórico Binário |
| ('P7_d_3 ', 'Criando consultas através da linguagem SQL para exportar informações e compartilhar com as áreas de negócio.') | Categórico Binário |
| ('P7_d_4 ', 'Utilizando API's para extrair dados e complementar minhas análises.') | Categórico Binário |
| ('P7_d_5 ', 'Realizando experimentos e estudos utilizando metodologias estatísticas como teste de hipótese, modelos de regressão etc.') | Categórico Binário |
| ('P7_d_6 ', 'Desenvolvendo/cuidando da manutenção de ETL's utilizando tecnologias como Talend, Pentaho, Airflow, Dataflow etc.') | Categórico Binário |
| ('P7_d_7 ', 'Atuando na modelagem dos dados, com o objetivo de criar conjuntos de dados, Data Warehouses, Data Marts etc.') | Categórico Binário |
| ('P7_d_8 ', 'Desenvolvendo/cuidando da manutenção de planilhas do Excel ou Google Sheets para atender as áreas de negócio.') | Categórico Binário |
| ('P7_d_9 ', 'Utilizando ferramentas avançadas de estatística como SAS, SPSS, Stata etc, para realizar análises.') | Categórico Binário |
| ('P7_d_10 ', 'Nenhuma das opções listadas refletem meu dia a dia.') | Categórico Binário |
| ('P8_a ', 'Quais das opções abaixo fazem parte da sua rotina no trabalho atual com ciência de dados?') | Categórico Polinomial Não Ordinal |
| ('P8_a_1 ', 'Estudos Ad-hoc com o objetivo de confirmar hipóteses, realizar modelos preditivos, forecasts, análise de cluster para resolver problemas pontuais e responder perguntas das áreas de negócio.') | Categórico Binário |
| ('P8_a_2 ', 'Sou responsável pela coleta e limpeza dos dados que uso para análise e modelagem.') | Categórico Binário |
| ('P8_a_3 ', 'Sou responsável por entrar em contato com os times de negócio para definição do problema, identificar a solução e apresentação de resultados.') | Categórico Binário |
| ('P8_a_4 ', 'Desenvolvo modelos de Machine Learning com o objetivo de colocar em produção em sistemas (produtos de dados).') | Categórico Binário |
| ('P8_a_5 ', 'Sou responsável por colocar modelos em produção, criar os pipelines de dados, APIs de consumo e monitoramento.') | Categórico Binário |
| ('P8_a_6 ', 'Cuido da manutenção de modelos de Machine Learning já em produção, atuando no monitoramento, ajustes e refatoração quando necessário.') | Categórico Binário |
| ('P8_a_7 ', 'Realizo construções de dashboards em ferramentas de BI como PowerBI, Tableau, Looker, Qlik, etc') | Categórico Binário |
| ('P8_a_8 ', 'Utilizo ferramentas avançadas de estatística como SAS, SPSS, Stata etc, para realizar análises estatísticas e ajustar modelos.') | Categórico Binário |
| ('P8_a_9 ', 'Crio e dou manutenção em ETLs, DAGs e automações de pipelines de dados.') | Categórico Binário |
| ('P8_a_10 ', 'Crio e gerencio soluções de Feature Store e cultura de MLOps.') | Categórico Binário |
| ('P8_a_11 ', 'Sou responsável por criar e manter a infra que meus modelos e soluções rodam (clusters, servidores, API, containers, etc.)') | Categórico Binário |
| ('P8_a_12 ', 'Treino e aplico LLM's para solucionar problemas de negócio.') | Categórico Binário |
| ('P8_b ', 'Quais as técnicas e métodos listados abaixo você costuma utilizar no trabalho?') | Categórico Polinomial Não Ordinal |
| ('P8_b_1 ', 'Utilizo modelos de regressão (linear, logística, GLM)') | Categórico Binário |
| ('P8_b_2 ', 'Utilizo redes neurais ou modelos baseados em árvore para criar modelos de classificação') | Categórico Binário |
| ('P8_b_3 ', 'Desenvolvo sistemas de recomendação (RecSys)') | Categórico Binário |
| ('P8_b_4 ', 'Utilizo métodos estatísticos Bayesianos para analisar dados') | Categórico Binário |
| ('P8_b_5 ', 'Utilizo técnicas de NLP (Natural Language Processing) para análisar dados não-estruturados') | Categórico Binário |
| ('P8_b_6 ', 'Utilizo métodos estatísticos clássicos (Testes de hipótese, análise multivariada, sobrevivência, dados longitudinais, inferência estatistica) para analisar dados') | Categórico Binário |
| ('P8_b_7 ', 'Utilizo cadeias de Markov ou HMM's para realizar análises de dados') | Categórico Binário |
| ('P8_b_8 ', 'Desenvolvo técnicas de Clusterização (K-means, Spectral, DBScan etc)') | Categórico Binário |
| ('P8_b_9 ', 'Realizo previsões através de modelos de Séries Temporais (Time Series)') | Categórico Binário |
| ('P8_b_10 ', 'Utilizo modelos de Reinforcement Learning (aprendizado por reforço)') | Categórico Binário |
| ('P8_b_11 ', 'Utilizo modelos de Machine Learning para detecção de fraude') | Categórico Binário |
| ('P8_b_12 ', 'Utilizo métodos de Visão Computacional') | Categórico Binário |
| ('P8_b_13 ', 'Utilizo modelos de Detecção de Churn') | Categórico Binário |
| ('P8_b_14 ', 'Utilizo LLM's para solucionar problemas de negócio') | Categórico Binário |
| ('P8_3 ', 'Quais dessas tecnologias fazem parte do seu dia a dia como cientista de dados?') | Categórico Polinomial Não Ordinal |
| ('P8_c_1 ', 'Ferramentas de BI (PowerBI, Looker, Tableau, Qlik etc)') | Categórico Binário |
| ('P8_c_2 ', 'Planilhas (Excel, Google Sheets etc)') | Categórico Binário |
| ('P8_c_3 ', 'Ambientes de desenvolvimento local (R-studio, JupyterLab, Anaconda)') | Categórico Binário |
| ('P8_c_4 ', 'Ambientes de desenvolvimento na nuvem (Google Colab, AWS Sagemaker, Kaggle Notebooks etc)') | Categórico Binário |
| ('P8_c_5 ', 'Ferramentas de AutoML (Datarobot, H2O, Auto-Keras etc)') | Categórico Binário |
| ('P8_c_6 ', 'Ferramentas de ETL (Apache Airflow, NiFi, Stitch, Fivetran, Pentaho etc)') | Categórico Binário |
| ('P8_c_7 ', 'Plataformas de Machine Learning (TensorFlow, Azure Machine Learning, Kubeflow etc)') | Categórico Binário |
| ('P8_c_8 ', 'Feature Store (Feast, Hopsworks, AWS Feature Store, Databricks Feature Store etc)') | Categórico Binário |
| ('P8_c_9 ', 'Sistemas de controle de versão (Github, DVC, Neptune, Gitlab etc)') | Categórico Binário |
| ('P8_c_10 ', 'Plataformas de Data Apps (Streamlit, Shiny, Plotly Dash etc)') | Categórico Binário |
| ('P8_c_11 ', 'Ferramentas de estatística avançada como SPSS, SAS, etc.') | Categórico Binário |
| ('P8_d ', 'Em qual das opções abaixo você gasta a maior parte do seu tempo no trabalho?') | Categórico Polinomial Não Ordinal |
| ('P8_d_1 ', 'Estudos Ad-hoc com o objetivo de confirmar hipóteses, realizar modelos preditivos, forecasts, análise de cluster para resolver problemas pontuais e responder perguntas das áreas de negócio.') | Categórico Binário |
| ('P8_d_2 ', 'Coletando e limpando os dados que uso para análise e modelagem.') | Categórico Binário |
| ('P8_d_3 ', 'Entrando em contato com os times de negócio para definição do problema, identificar a solução e apresentação de resultados.') | Categórico Binário |
| ('P8_d_4 ', 'Desenvolvendo modelos de Machine Learning com o objetivo de colocar em produção em sistemas (produtos de dados).') | Categórico Binário |
| ('P8_d_5 ', 'Colocando modelos em produção, criando os pipelines de dados, APIs de consumo e monitoramento.') | Categórico Binário |
| ('P8_d_6 ', 'Cuidando da manutenção de modelos de Machine Learning já em produção, atuando no monitoramento, ajustes e refatoração quando necessário.') | Categórico Binário |
| ('P8_d_7 ', 'Realizando construções de dashboards em ferramentas de BI como PowerBI, Tableau, Looker, Qlik, etc.') | Categórico Binário |
| ('P8_d_8 ', 'Utilizando ferramentas avançadas de estatística como SAS, SPSS, Stata etc, para realizar análises.') | Categórico Binário |
| ('P8_d_9 ', 'Criando e dando manutenção em ETLs, DAGs e automações de pipelines de dados.') | Categórico Binário |
| ('P8_d_10 ', 'Criando e gerenciando soluções de Feature Store e cultura de MLOps.') | Categórico Binário |
| ('P8_d_11 ', 'Criando e mantendo a infra que meus modelos e soluções rodam (clusters, servidores, API, containers, etc.)') | Categórico Binário |
| ('P8_d_12 ', 'Treinando e aplicando LLM's para solucionar problemas de negócio.') | Categórico Binário |
</details>

#### `PNAD_Roubos_Furtos_Brasil_2023`

Esta base de dados contém informações agregadas sobre ocorrências de roubos e furtos no Brasil, organizadas por grande região. Os dados abrangem diferentes categorias de ocorrência, como roubos de veículos, em domicílios e em locais públicos, possibilitando uma análise do perfil e distribuição regional desses eventos. Essa base pode ser utilizada para identificar padrões territoriais de criminalidade patrimonial, auxiliando em estudos sobre segurança pública e desigualdades regionais.

- Atributos da Base

| Atributo             | Tipo                  | Descrição |
|----------------------|-----------------------|-----------|
| Grande Região        | Categórico Nominal    | Região do Brasil onde o crime ocorreu (Sudeste, Nordeste, Norte, Sul, Centro-Oeste) |
| Veículo              | Quantitativo Discreto | Total de ocorrências envolvendo qualquer tipo de veículo |
| Carro                | Quantitativo Discreto | Total de ocorrências envolvendo carros |
| Moto                 | Quantitativo Discreto | Total de ocorrências envolvendo motos |
| Bicicleta            | Quantitativo Discreto | Total de ocorrências envolvendo bicicletas |
| Domicílio            | Quantitativo Discreto | Total de ocorrências registradas em residências |
| Fora do domicílio    | Quantitativo Discreto | Total de ocorrências em locais públicos ou externos |

#### `PNAD Média Horas Semanais de Trabalho Doméstico por Cor ou Raça - Brasil`

Esta base de dados apresenta a média de horas semanais dedicadas ao trabalho doméstico por diferentes grupos raciais no Brasil. Os dados são úteis para identificar desigualdades na distribuição do trabalho não remunerado e suas possíveis relações com raça/cor.

- Atributos da Base

| Atributo     | Tipo                   | Dados                        |
|--------------|------------------------|------------------------------|
| Cor ou raça  | Categórico Nominal     | Branca; Preta; Parda; Total |
| Total        | Quantitativo Contínuo  | Horas semanais (ex: 17,4)   |


###    Descrição de dados

### `Análise Exploratória dos Dados - State_of_data_BR_2023_Kaggle - df_survey_2023`

#### 1. Distribuição por Gênero

- **Moda:** Masculino (3975 respostas)
- **Distribuição:**
  - Feminino: **24,46%**
  - Masculino: **75,23%**
  - Outro: **0,17%**
  - Prefiro não informar: **0,30%**
    
![genero](https://github.com/user-attachments/assets/3df947d6-bf29-48f3-a2ff-c1cdfeaa71be)

#### 2. Pessoas com Deficiência (PCD)

- **Moda:** Não (5156 respostas)
- **Distribuição:**
  - Não: **97,22%**
  - Prefiro não informar: **0,49%**
  - Sim: **2,09%**
    
![pcd](https://github.com/user-attachments/assets/dc9d3912-e8c3-436f-a168-727c6a638f13)

#### 3. Estado de Residência

- **Moda:** São Paulo (2073 respostas)
- **Estados com maior representação:**
  - São Paulo (SP): **39,42%**
  - Minas Gerais (MG): **10,59%**
  - Rio de Janeiro (RJ): **8,31%**
  - Paraná (PR): **7,99%**
  - Rio Grande do Sul (RS): **5,54%**
 
![Estado](https://github.com/user-attachments/assets/69bdc86a-2929-417c-838f-3f1a2e3c4a64)

#### 4. Nível Profissional

- **Moda:** Sênior (1419 respostas)
- **Distribuição:**
  - Júnior: **27,46%**
  - Pleno: **36,56%**
  - Sênior: **36,98%**
 
![Nivel](https://github.com/user-attachments/assets/d760284c-8ba4-484a-813a-3e1ed06a9e58)

#### 5. Faixa Salarial

- **Moda:** de R$ 8.001/mês a R$ 12.000/mês (1026 respostas)
- **Faixas com maior representação:**
  - R$ 8.001 a R$ 12.000: **18,85%**
  - R$ 12.001 a R$ 16.000: **11,95%**
  - R$ 4.001 a R$ 6.000: **13,68%**
  - R$ 6.001 a R$ 8.000: **11,71%**

![salario](https://github.com/user-attachments/assets/fd0ad9d4-b767-4fb6-a390-d8245c6c268d)

#### 6. Forma de Trabalho Atual

- **Moda:** Modelo 100% remoto (2201 respostas)
- **Distribuição:**
  - Modelo 100% presencial: **14,91%**
  - Modelo 100% remoto: **41,58%**
  - Modelo híbrido com dias fixos: **14,91%**
  - Modelo híbrido flexível: **18,38%**

![FormaTrabalho](https://github.com/user-attachments/assets/786e5481-844d-4005-bb91-a9e45279475b)

#### 7. Forma de Trabalho Ideal

- **Moda:** Modelo híbrido flexível (2144 respostas)
- **Distribuição:**
  - Modelo 100% presencial: **1,81%**
  - Modelo 100% remoto: **40,27%**
  - Modelo híbrido com dias fixos: **7,37%**
  - Modelo híbrido flexível: **40,69%**

![formaIdeal](https://github.com/user-attachments/assets/6621eb7f-6d8c-4c6c-b494-f6fb14dffb8d)

#### **1. Comparação entre Nível Profissional e Forma de Trabalho**

- **Moda:** Profissionais **Sêniores** preferem o modelo **100% remoto** (**796 respostas**), enquanto os **Plenos** também escolhem majoritariamente o **100% remoto** (**673 respostas**). Já os **Júniores** têm uma distribuição mais equilibrada entre **100% remoto** (395 respostas) e **100% presencial** (283 respostas).  

##### **Distribuição dentro de cada Nível Profissional**  

- **Sênior**  
  - **100% presencial:** **9,02%** (128)  
  - **100% remoto:** **56,08%** (796)  
  - **Híbrido fixo:** **14,52%** (206)  
  - **Híbrido flexível:** **20,36%** (289)  

- **Pleno**  
  - **100% presencial:** **16,10%** (224)  
  - **100% remoto:** **48,35%** (673)  
  - **Híbrido fixo:** **17,11%** (238)  
  - **Híbrido flexível:** **18,47%** (257)  

- **Júnior**  
  - **100% presencial:** **27,06%** (283)  
  - **100% remoto:** **37,75%** (395)  
  - **Híbrido fixo:** **17,78%** (186)  
  - **Híbrido flexível:** **17,41%** (182)  

- **Não informado**  
  - **100% presencial:** **17,30%** (155)  
  - **100% remoto:** **37,61%** (337)  
  - **Híbrido fixo:** **17,86%** (160)  
  - **Híbrido flexível:** **27,23%** (244)  

![NivelXmodelo](https://github.com/user-attachments/assets/cf59df5f-0648-4393-8ebf-68c8e2d18607)

#### **2. Comparação entre Estados e Forma de Trabalho**  

- **Moda:** O modelo **100% remoto** é o mais comum em todos os estados, sendo **São Paulo (SP)** o que mais concentra profissionais nesse modelo (**759 respostas**), seguido por **Minas Gerais (MG) (252 respostas)** e **Rio de Janeiro (RJ) (194 respostas)**.   

##### **Distribuição por Estado (%)**  

###### **São Paulo (SP)**  
- **100% presencial:** **11,29%** (214)  
- **100% remoto:** **40,06%** (759)  
- **Híbrido fixo:** **22,48%** (426)  
- **Híbrido flexível:** **26,17%** (496)  

###### **Minas Gerais (MG)**  
- **100% presencial:** **17,46%** (88)  
- **100% remoto:** **50,00%** (252)  
- **Híbrido fixo:** **12,50%** (63)  
- **Híbrido flexível:** **20,04%** (101)  

###### **Rio de Janeiro (RJ)**  
- **100% presencial:** **11,36%** (45)  
- **100% remoto:** **48,99%** (194)  
- **Híbrido fixo:** **18,94%** (75)  
- **Híbrido flexível:** **20,71%** (82)  

###### **Paraná (PR)**  
- **100% presencial:** **21,54%** (84)  
- **100% remoto:** **51,03%** (199)  
- **Híbrido fixo:** **15,64%** (61)  
- **Híbrido flexível:** **11,79%** (46)  

###### **Rio Grande do Sul (RS)**  
- **100% presencial:** **18,70%** (49)  
- **100% remoto:** **48,85%** (128)  
- **Híbrido fixo:** **8,40%** (22)  
- **Híbrido flexível:** **24,05%** (63)  

###### **Santa Catarina (SC)**  
- **100% presencial:** **15,38%** (36)  
- **100% remoto:** **50,85%** (119)  
- **Híbrido fixo:** **13,25%** (31)  
- **Híbrido flexível:** **20,51%** (48)  

###### **Distrito Federal (DF)**  
- **100% presencial:** **23,02%** (35)  
- **100% remoto:** **43,42%** (66)  
- **Híbrido fixo:** **19,74%** (30)  
- **Híbrido flexível:** **13,82%** (21)  

![EstadoXmodelo](https://github.com/user-attachments/assets/69b4db17-d1e1-41a0-8338-d0bd773d0eca)

#### **3. Comparação entre Faixa Salarial e Modelo de Trabalho**  

- **Moda:** O modelo **100% remoto** se destaca nas faixas salariais mais altas, especialmente **acima de R$ 8.000/mês**. Já o modelo **100% presencial** tem maior concentração em salários **abaixo de R$ 6.000/mês**.  

##### **Distribuição por Faixa Salarial (%)**  

###### **Faixa: R$ 8.001/mês a R$ 12.000/mês**  
- **100% presencial:** **11,02%** (113)  
- **100% remoto:** **51,08%** (524)  
- **Híbrido fixo:** **17,45%** (179)  
- **Híbrido flexível:** **20,45%** (210)  

###### **Faixa: R$ 4.001/mês a R$ 6.000/mês**  
- **100% presencial:** **21,61%** (161)  
- **100% remoto:** **41,61%** (310)  
- **Híbrido fixo:** **20,13%** (150)  
- **Híbrido flexível:** **16,64%** (124)  

###### **Faixa: R$ 12.001/mês a R$ 16.000/mês**  
- **100% presencial:** **6,77%** (44)  
- **100% remoto:** **56,00%** (364)  
- **Híbrido fixo:** **12,92%** (84)  
- **Híbrido flexível:** **24,31%** (158)  

###### **Faixa: R$ 6.001/mês a R$ 8.000/mês**  
- **100% presencial:** **13,50%** (86)  
- **100% remoto:** **45,68%** (291)  
- **Híbrido fixo:** **16,64%** (106)  
- **Híbrido flexível:** **24,18%** (154)  

###### **Faixa: R$ 3.001/mês a R$ 4.000/mês**  
- **100% presencial:** **32,39%** (114)  
- **100% remoto:** **33,81%** (119)  
- **Híbrido fixo:** **20,45%** (72)  
- **Híbrido flexível:** **13,35%** (47)  

###### **Faixa: R$ 16.001/mês a R$ 20.000/mês**  
- **100% presencial:** **7,92%** (26)  
- **100% remoto:** **53,66%** (176)  
- **Híbrido fixo:** **17,38%** (57)  
- **Híbrido flexível:** **21,04%** (69)  

###### **Faixa: R$ 2.001/mês a R$ 3.000/mês**  
- **100% presencial:** **39,93%** (115)  
- **100% remoto:** **30,56%** (88)  
- **Híbrido fixo:** **16,32%** (47)  
- **Híbrido flexível:** **13,19%** (38)  

###### **Faixa: R$ 1.001/mês a R$ 2.000/mês**  
- **100% presencial:** **35,81%** (77)  
- **100% remoto:** **36,28%** (78)  
- **Híbrido fixo:** **13,95%** (30)  
- **Híbrido flexível:** **13,95%** (30)  

###### **Faixa: Acima de R$ 25.000/mês**  
- **100% presencial:** **14,28%** (35)  
- **100% remoto:** **51,42%** (126)  
- **Híbrido fixo:** **17,14%** (42)  
- **Híbrido flexível:** **17,14%** (42)  

![SalarioXmodelo](https://github.com/user-attachments/assets/0cbda8e9-5f41-4ef6-8e88-ff2f3673124c)


### Análise Exploratória dos Dados - PNAD Roubos e Furtos (Brasil)

Este documento apresenta a análise exploratória dos dados da PNAD sobre roubos e furtos no Brasil, organizados por grande região e por tipo de ocorrência (veículos, carros, motos, bicicletas, domicílios e fora do domicílio). O objetivo é identificar padrões regionais e categorias mais recorrentes.

#### 1. Total de Ocorrências por Região (Soma Geral)

- **Moda:** Sudeste (814 ocorrências)
- **Distribuição percentual:**
  - Sudeste: **32,64%**
  - Nordeste: **29,41%**
  - Norte: **11,44%**
  - Sul: **5,21%**
  - Centro-Oeste: **5,17%**

![Soma](https://github.com/user-attachments/assets/cf308f76-285a-430b-9e39-2ac119e8c1b3)

#### 2. Ocorrências por Categoria e Região

- **Categoria mais frequente no geral:** Fora do domicílio (1398 ocorrências)
- **Categorias com maior concentração por região:**
  - Sudeste: Fora do domicílio (565 ocorrências)
  - Nordeste: Fora do domicílio (487 ocorrências)
  - Norte: Fora do domicílio (190 ocorrências)
  - Sul: Fora do domicílio (74 ocorrências)
  - Centro-Oeste: Fora do domicílio (82 ocorrências)

![SomaCategoria](https://github.com/user-attachments/assets/37ef8272-211b-43e1-adb9-35dd1358c3d5)

#### 3. Domicílio x Fora do Domicílio por Região

- **Moda:** Fora do domicílio em todas as regiões
- **Distribuição total:**
  - Domicílio: **195 ocorrências**
  - Fora do domicílio: **1398 ocorrências**

![DomicilioXforaDomicilio](https://github.com/user-attachments/assets/9114ae1b-2fef-48a2-9c5b-56b1c4eb9012)


### Análise Exploratória dos Dados - PNAD Média Horas de Trabalho Doméstico por Cor ou Raça (Brasil)

Este documento apresenta uma análise exploratória sobre o tempo médio semanal dedicado ao trabalho doméstico, categorizado por cor ou raça no Brasil. Os dados analisados permitem observar disparidades sutis, mas relevantes, que refletem aspectos sociais e estruturais presentes na divisão de tarefas não remuneradas.

#### 1. Horas Semanais de Trabalho Doméstico por Cor ou Raça
- **Média Geral:** 17 horas/semana
- **Distribuição por grupo racial:**
  - **Branca:** 16,5 horas
  - **Preta:** 17,1 horas
  - **Parda:** 17,4 horas
  
![HorasDomesticas](https://github.com/user-attachments/assets/e3e3678b-dee1-47b5-8a7e-29c5c2a3e049)


## Preparação dos dados

A preparação dos dados consiste dos seguintes passos:

### Seleção de Atributos:
#### `State_of_data_BR_2023_Kaggle - df_survey_2023`
* ('P1_b ', 'Genero')
* ('P1_d ', 'PCD')
* ('P1_i ', 'Estado onde mora')
* ('P2_f ', 'Cargo Atual')
* ('P2_g ', 'Nivel')
* ('P2_h ', 'Faixa salarial')
* ('P2_o_4 ', 'Flexibilidade de trabalho remoto')
* ('P2_r ', 'Atualmente qual a sua forma de trabalho?')
* ('P2_s ', 'Qual a forma de trabalho ideal para você?')

#### `PNAD_Roubos_Furtos - df_roubos_furtos`
* ('Grande Região', 'Região geográfica do Brasil')
* ('Veículo', 'Ocorrências de roubo/furto de veículos em geral')
* ('Carro', 'Ocorrências de roubo/furto de carros')
* ('Moto', 'Ocorrências de roubo/furto de motos')
* ('Bicicleta', 'Ocorrências de roubo/furto de bicicletas')
* ('Domicílio', 'Ocorrências de roubo/furto dentro do domicílio')
* ('Fora do domicílio', 'Ocorrências de roubo/furto fora do domicílio')
* ('Soma', 'Total de ocorrências registradas por região')

#### `PNAD_Tempo_Trab_Doméstico - df_trabalho_domestico`

* ('Cor ou raça', 'Grupo racial da pessoa entrevistada')
* ('Total', 'Quantidade média de horas semanais dedicadas ao trabalho doméstico')

## Indução de modelos

### Modelo 1: árvore de decisão

### Importção de Bibliotecas
```python
!pip install pandas scikit-learn matplotlib pydotplus dtreeviz

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
```
### Transformação de Dados
```python
df = pd.read_csv("data_tratada.csv")

print("\nDimensões:", df.shape)
print("\nCampos:", df.columns)
print(df.describe())

# Remover registros com alvo ausente
df = df.dropna(subset=['Forma de trabalho ideal'])

# Separar variáveis independentes e alvo
X_dict = df.drop(columns=['Forma de trabalho ideal', 'Cargo atual']).to_dict(orient='records')
vect = DictVectorizer(sparse=False)
X = vect.fit_transform(X_dict)

le = LabelEncoder()
y = le.fit_transform(df['Forma de trabalho ideal'])

# Dividir os dados corretamente
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

print("Shape dos dados de treino:", X_train.shape)
print("Shape dos dados de teste:", X_test.shape)
```
![Transformação de Dados](https://github.com/user-attachments/assets/b6c22b4d-c529-4099-9024-bd8a5e9db735)

### Indução do Modelo
```python
# Definir modelo com limitação de profundidade e folhas mínimas
treeForma = DecisionTreeClassifier(random_state=0, criterion='entropy', max_depth=5, min_samples_leaf=4)
treeForma.fit(X_train, y_train)

# Avaliação no conjunto de teste
y_pred = treeForma.predict(X_test)
print("Acurácia no teste:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
cnf_matrix = confusion_matrix(y_test, y_pred)
cnf_table = pd.DataFrame(cnf_matrix, index=[f"Real={c}" for c in le.classes_], columns=[f"Prev={c}" for c in le.classes_])
print(cnf_table)

```
![Indução do Modelo](https://github.com/user-attachments/assets/ffb88ccd-1682-4f3f-a75c-17b1f18e9d0c)

### Exibição das Importancias dos Atributos 
```python
# Exibir importâncias dos atributos
importances = pd.Series(treeForma.feature_importances_, index=vect.feature_names_)
importances = importances[importances > 0].sort_values(ascending=False)
print("\nImportância dos atributos:")
print(importances)

# Visualizar graficamente
importances.plot(kind='barh', figsize=(10, 6), title='Importância dos Atributos')
plt.gca().invert_yaxis()
plt.show()
```
![Exibicão Importancia Atributos](https://github.com/user-attachments/assets/5790bd38-25dc-4d93-b137-a0413ee32bf4)

![Exibicão Importancia Atributos Graficamente](https://github.com/user-attachments/assets/5bcbfd4a-e76e-44b8-9633-5d0eadcd1f31)

### Exibição da Arvore de Decisão
```python
# Visualizar a árvore com profundidade limitada
from sklearn import tree

plt.figure(figsize=(20, 10))
tree.plot_tree(treeForma,
               feature_names=vect.get_feature_names_out(),  # alternativo mais robusto
               class_names=[str(c) for c in le.classes_],    # garantir strings
               filled=True,
               rounded=True)
plt.show()
```
![Exibição da Árvore de Decisão](https://github.com/user-attachments/assets/4eeb09b2-e703-45dd-8f9a-68201ed24ed2)

### Modelo 2: Random Forest

### Importação das bibliotecas e do dataset
Importa a biblioteca pandas, carrega a base de dados CSV a partir do Google Drive e exibe as primeiras 5 linhas da tabela para visualização.
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction import DictVectorizer

data = pd.read_csv('dataset_tratado.csv')

pd.set_option('display.max_columns', None)

print(f'Dimensões: {data.shape}')
print(f'Colunas: {data.columns}')

data.head(5)
```
### Gerando base de treinamento e teste
Seleciona os dados de teste e o alvo e codifica os valores categóricos para numéricos e divide a base de dados em treino (70%) e teste (30%)
```python
X_dict = data.drop(columns=['Roubos de veículo', 'Roubos de carro', 'Roubos de moto', 'Roubos de bicicleta', 'Roubos fora do domicílio', 'Total de roubos', 'Forma de trabalho ideal'], axis=1).T.to_dict().values()
vect = DictVectorizer(sparse=False)
X = vect.fit_transform(X_dict)

le = LabelEncoder()
y = le.fit_transform(data.iloc[:, data.shape[1]-1])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
```
### Treinando o Random Forest
Treina o RandomForest e guarda todas as acurácias em um array, foi separado duas árvores para fins de comparação. Uma com melhor desempenho de acurácia e outra com o pior desempenho
```python
forest = RandomForestClassifier(random_state=42, criterion='entropy', max_depth=7)
forest.fit(X_train, y_train)
print(f'Acurácia do treinamento: {forest.score(X_train, y_train)}')

accuracies = {}

for i, tree_model in enumerate(forest.estimators_):
  y_pred = tree_model.predict(X_test)
  acc_score = accuracy_score(y_test, y_pred)
  accuracies[i] = acc_score

best_tree = max(accuracies, key=accuracies.get)
worst_tree = min(accuracies, key=accuracies.get)

print(f'Acurácia da melhor árvore: {accuracies[best_tree]}')
print(f'Acurácia da pior árvore: {accuracies[worst_tree]}')

best_y_pred = forest.estimators_[best_tree].predict(X_test)
worst_y_pred = forest.estimators_[worst_tree].predict(X_test)

print('\nClassification Report da melhor árvore:')
print(classification_report(y_test, best_y_pred))
print('\nClassification Report da pior árvore:')
print(classification_report(y_test, worst_y_pred))
```
```
Acurácia do treinamento: 0.8260869565217391
Acurácia da melhor árvore: 0.7630161579892281
Acurácia da pior árvore: 0.5915619389587073

Classification Report da melhor árvore:
              precision    recall  f1-score   support

           0       0.00      0.00      0.00        19
           1       0.82      0.68      0.74       524
           2       0.73      0.87      0.79       571

    accuracy                           0.76      1114
   macro avg       0.52      0.51      0.51      1114
weighted avg       0.76      0.76      0.76      1114


Classification Report da pior árvore:
              precision    recall  f1-score   support

           0       0.00      0.00      0.00        19
           1       0.59      0.55      0.57       524
           2       0.60      0.65      0.62       571

    accuracy                           0.59      1114
   macro avg       0.40      0.40      0.40      1114
weighted avg       0.58      0.59      0.59      1114
```
### Matriz de confusão da melhor árvore
Aqui foi feita a visualização da matriz de confusão da árvore com melhor desempenho, sendo mostrado uma pequena confusão entre remoto e hibrído. O modelo presencial foi completamente desconsiderado em função de ter poucos dados relacionados a esse modelo
```python
from sklearn.metrics import ConfusionMatrixDisplay
from matplotlib import pyplot as plt

# Melhor arvore
best_cnf_matrix = confusion_matrix(y_test, best_y_pred)
print(f'Matriz de confusão: \n{best_cnf_matrix}')

df_cnf_matrix = pd.DataFrame(best_cnf_matrix, index=le.classes_, columns=le.classes_)
print(f'Matriz de confusão formatada: \n{df_cnf_matrix}')

display = ConfusionMatrixDisplay.from_estimator(forest.estimators_[best_tree], X_test, y_test, display_labels=le.classes_, cmap=plt.cm.Greens)

plt.xticks(rotation=90)
plt.show()
```
```
Matriz de confusão: 
[[  0   1  18]
 [  2 356 166]
 [  1  76 494]]
Matriz de confusão formatada: 
                        Modelo 100% presencial  Modelo 100% remoto  \
Modelo 100% presencial                       0                   1   
Modelo 100% remoto                           2                 356   
Modelo híbrido                               1                  76   

                        Modelo híbrido  
Modelo 100% presencial              18  
Modelo 100% remoto                 166  
Modelo híbrido                     494  
```
![image](https://github.com/user-attachments/assets/7a692d74-e83f-41c1-87fd-4353d81c79f6)
### Matriz de confusão da pior árvore
Enquanto aqui, é descrito a matriz de confusão da da árvore com menor desempenho. Aqui a confusão entre hibrido e remoto é mais generalizada
```python
from sklearn.metrics import ConfusionMatrixDisplay
from matplotlib import pyplot as plt

# Melhor arvore
worst_cnf_matrix = confusion_matrix(y_test, worst_y_pred)
print(f'Matriz de confusão: \n{best_cnf_matrix}')

df_cnf_matrix = pd.DataFrame(worst_cnf_matrix, index=le.classes_, columns=le.classes_)
print(f'Matriz de confusão formatada: \n{df_cnf_matrix}')

display = ConfusionMatrixDisplay.from_estimator(forest.estimators_[worst_tree], X_test, y_test, display_labels=le.classes_, cmap=plt.cm.Greens)

plt.xticks(rotation=90)
plt.show()
```
```
Matriz de confusão: 
[[  0   1  18]
 [  2 356 166]
 [  1  76 494]]
Matriz de confusão formatada: 
                        Modelo 100% presencial  Modelo 100% remoto  \
Modelo 100% presencial                       0                   1   
Modelo 100% remoto                           1                 290   
Modelo híbrido                               4                 198   

                        Modelo híbrido  
Modelo 100% presencial              18  
Modelo 100% remoto                 233  
Modelo híbrido                     369  
```
![image](https://github.com/user-attachments/assets/e6bd93ce-b71d-4b2b-a944-9ae2a6525fc6)
### Visualização de um gráfico de importância da melhor árvore
Foi feito uma vizualização dos valores mais importantes na construção da melhor árvore. Os atributos mais importantes levam em consideração a forma de trabalho atual do profissional e a atitude do profissional caso a empresa adote o modelo 100% presencial
```python
best_importance = forest.estimators_[best_tree].feature_importances_

best_importance_series = pd.Series(best_importance, index=vect.get_feature_names_out())
best_importance_series = best_importance_series.sort_values(ascending=False).head(10)

print(f'Importância das variáveis: \n{best_importance_series}')

plt.figure(figsize=(5, 5))
best_importance_series.plot(kind='barh', legend=False)
plt.title('Importância das variáveis (Melhor árvore)')
plt.gca().invert_yaxis()
```
```
Importância das variáveis: 
Decisão da empresa para modelo 100% presencial=Vou aceitar e retornar ao modelo 100% presencial               0.311739
Forma de trabalho atual=Modelo híbrido                                                                        0.212135
Decisão da empresa para modelo 100% presencial=Vou procurar outra oportunidade no modelo híbrido ou remoto    0.096771
Decisão da empresa para modelo 100% presencial=Vou procurar outra oportunidade no modelo 100% remoto          0.085514
Forma de trabalho atual=Modelo 100% remoto                                                                    0.064423
Área de formação=Outra opção                                                                                  0.014356
Faixa salarial=de R$ 4.001/mês a R$ 6.000/mês                                                                 0.013847
Nível=Sênior                                                                                                  0.011894
Estado onde mora=Rio Grande do Sul (RS)                                                                       0.010316
Cor/Raça=Branca                                                                                               0.010064
dtype: float64
```
![image](https://github.com/user-attachments/assets/d961aa11-bab1-402c-ace4-7ff416af7935)
### Visualização do gráfico de importância da pior árvore
Entretanto, aqui a visualização dos atributos mais importantes deu mais ênfase em aspectos demográficos do que a atitude do profissional em caso da empresa adotar 100% presencial e o modelo de trabalho atual
```python
worst_importance = forest.estimators_[worst_tree].feature_importances_

worst_importance_series = pd.Series(worst_importance, index=vect.get_feature_names_out())
worst_importance_series = worst_importance_series.sort_values(ascending=False).head(10)

print(f'\nImportância das variáveis: \n{worst_importance_series}')

plt.figure(figsize=(5, 5))
worst_importance_series.plot(kind='barh', legend=False)
plt.title('Importância das variáveis (Pior árvore)')
plt.gca().invert_yaxis()
```
```
Importância das variáveis: 
Decisão da empresa para modelo 100% presencial=Vou aceitar e retornar ao modelo 100% presencial    0.352205
Forma de trabalho atual=Modelo 100% remoto                                                         0.093790
Região onde mora=Nordeste                                                                          0.044124
Faixa salarial=de R$ 6.001/mês a R$ 8.000/mês                                                      0.035272
Cargo atual=Analista de Dados/Data Analyst                                                         0.027648
Forma de trabalho atual=Modelo 100% presencial                                                     0.027511
Gênero=Masculino                                                                                   0.023162
Idade                                                                                              0.023008
Faixa salarial=de R$ 20.001/mês a R$ 25.000/mês                                                    0.022522
Nivel de segurança=Moderado                                                                        0.022458
```
![image](https://github.com/user-attachments/assets/06480712-f8e0-4364-8740-1adceb3c5b9a)
### Visualização do RandomForest
Uma vizualização de todas as 100 árvores com suas respectivas acurácias
```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
plt.plot(range(len(accuracies.items())), accuracies.values(), marker='o', linestyle='-', color='blue')
plt.title('Acurácia do Modelo Random Forest')
plt.xlabel('Número de Árvores')
plt.ylabel('Acurácia')
plt.ylim(0, 1)
plt.grid(True)
plt.show()
```
![image](https://github.com/user-attachments/assets/213544e1-4510-448b-8c87-ea7af2081315)
### Visualização da Árvore com melhor desempenho
```python
import pydotplus
from sklearn import tree
from IPython.display import Image

dot_data = tree.export_graphviz(forest.estimators_[best_tree], out_file=None, feature_names=vect.get_feature_names_out(), class_names=le.classes_, filled=True, rounded=True, special_characters=True)

graph = pydotplus.graph_from_dot_data(dot_data)
Image(graph.create_png())
```
![image](https://github.com/user-attachments/assets/96c40ac2-74c9-4699-8826-e9fada9535d8)
### Visualização da Árvore com pior desempenho
```python
import pydotplus
from sklearn import tree
from IPython.display import Image

dot_data = tree.export_graphviz(forest.estimators_[worst_tree], out_file=None, feature_names=vect.get_feature_names_out(), class_names=le.classes_, filled=True, rounded=True, special_characters=True)

graph = pydotplus.graph_from_dot_data(dot_data)
Image(graph.create_png())
```
![image](https://github.com/user-attachments/assets/575f77b2-a16a-48d2-8eb3-6eb5a5c4b6dc)
## Resultados

### Resultados obtidos com o modelo 1.

#### Análise da Matriz de Confusão

 Resumo das Classes:
| Código | Classe                                                    |
|--------|-----------------------------------------------------------|
|   0    | Modelo 100% presencial                                    |
|   1    | Modelo 100% remoto                                        |
|   2    | Modelo híbrido com dias fixos de trabalho presencial      |
|   3    | Modelo híbrido flexível (o funcionário tem autonomia)     |

Acurácia geral:
65,3%
O modelo acerta aproximadamente dois terços das classificações.

Relatório de Classificação:
| Classe  | Precision | Recall | F1-Score | Support |
|---------|-----------|--------|----------|---------|
| 0       | 0.00      | 0.00   | 0.00     | 30      |
| 1       | 0.68      | 0.76   | 0.72     | 617     |
| 2       | 0.23      | 0.05   | 0.08     | 110     |
| 3       | 0.64      | 0.68   | 0.66     | 669     |

Análise da Matriz de Confusão:
Modelo 100% presencial (classe 0): Nenhum dos 30 exemplos foi corretamente classificado. A maioria foi confundida com o modelo híbrido flexível (26 casos) e alguns com o modelo 100% remoto (4 casos).
Modelo 100% remoto (classe 1): 468 de 617 exemplos foram classificados corretamente. Houve 144 confusões com o híbrido flexível, 5 com o híbrido fixo e nenhum com o presencial.
Modelo híbrido com dias fixos (classe 2): Apenas 5 de 110 exemplos foram corretamente classificados. A maioria foi confundida com o híbrido flexível (92 casos) e alguns com o remoto (13 casos).
Modelo híbrido flexível (classe 3): 458 de 669 exemplos foram classificados corretamente. Houve 199 confusões com o remoto, 12 com o híbrido fixo e nenhum com o presencial.

Matriz em forma de tabela/grafico:
| **Classe Real / Prevista**  | **Modelo 100% presencial** | **Modelo 100% remoto** | **Modelo híbrido fixo** | **Modelo híbrido flexível** |
| --------------------------- | -------------------------- | ---------------------- | ----------------------- | --------------------------- |
| **Modelo 100% presencial**  | 0                          | 4                      | 0                       | 26                          |
| **Modelo 100% remoto**      | 0                          | 468                    | 5                       | 144                         |
| **Modelo híbrido fixo**     | 0                          | 13                     | 5                       | 92                          |
| **Modelo híbrido flexível** | 0                          | 199                    | 12                      | 458                         |

### Interpretação Final

O modelo apresenta desempenho razoável para as classes **"100% remoto"** e **"híbrido flexível"**, mas tem desempenho muito baixo para **"100% presencial"** e **"híbrido fixo"**, que são frequentemente confundidas com as demais.

- Os **maiores erros** ocorrem entre as classes *"remoto"* e *"híbrido flexível"*, indicando **sobreposição de características** e possível dificuldade do modelo em distinguir nuances entre esses grupos.

- A classe **"100% presencial"** não é reconhecida pelo modelo, sugerindo **desbalanceamento** ou **falta de variáveis discriminantes** para esse perfil.

- O resultado sugere a necessidade de:
  - Ajustes no modelo,
  - Coleta de mais dados para as **classes minoritárias**, ou
  - Revisão das **variáveis preditoras** para melhorar a capacidade de distinção entre as categorias.

### Resultados obtidos com o modelo 2.

Matriz de Confusão - Melhor Árvore

| **Classe Real / Prevista** | **Híbrido fixo** | **Híbrido flexível** | **Modelo 100% presencial** | **Modelo 100% remoto** |
| -------------------------- | ---------------- | -------------------- | -------------------------- | ---------------------- |
| **Híbrido fixo**           | 7                | 53                   | 0                          | 9                      |
| **Híbrido flexível**       | 6                | 317                  | 0                          | 122                    |
| **Modelo 100% presencial** | 1                | 15                   | 0                          | 5                      |
| **Modelo 100% remoto**     | 1                | 103                  | 0                          | 312                    |

Matriz de Confusão - Pior Árvore

| **Classe Real / Prevista** | **Híbrido fixo** | **Híbrido flexível** | **Modelo 100% presencial** | **Modelo 100% remoto** |
| -------------------------- | ---------------- | -------------------- | -------------------------- | ---------------------- |
| **Híbrido fixo**           | 0                | 21                   | 0                          | 48                     |
| **Híbrido flexível**       | 2                | 172                  | 0                          | 271                    |
| **Modelo 100% presencial** | 0                | 7                    | 0                          | 14                     |
| **Modelo 100% remoto**     | 1                | 132                  | 0                          | 283                    |

Análise Detalhada das Métricas por Classe
Classe "Híbrido fixo" (69 casos totais):
Melhor árvore: Apenas 10.1% de precisão (7/69), com 76.8% dos casos incorretamente classificados como "Híbrido flexível" (53/69). Isso sugere que o modelo não consegue distinguir adequadamente entre os dois tipos de modelo híbrido.
Pior árvore: Colapso total com 0% de acertos. A confusão se divide entre "Híbrido flexível" (30.4%) e "Modelo 100% remoto" (69.6%), indicando que quando a árvore falha, ela tende a classificar erroneamente como trabalho remoto.

Classe "Híbrido flexível" (445 casos totais - classe majoritária):
Melhor árvore: Performance sólida com 71.2% de acertos (317/445). Os erros principais concentram-se em 27.4% classificados como "Modelo 100% remoto" (122/445), sugerindo sobreposição conceitual entre flexibilidade híbrida e trabalho remoto.
Pior árvore: Degradação significativa para 38.7% (172/445), com 60.9% dos casos incorretamente categorizados como "Modelo 100% remoto" (271/445). Isso revela instabilidade extrema na distinção entre modelos flexíveis.

Classe "Modelo 100% presencial" (21 casos totais - classe minoritária crítica):
Ambas as árvores: Falha completa com 0% de acertos, representando o maior problema do modelo. Na melhor árvore, 71.4% são confundidos com "Híbrido flexível" (15/21), enquanto na pior árvore a confusão se distribui mais uniformemente. Esta classe está sendo completamente absorvida pelas outras categorias.

Classe "Modelo 100% remoto" (416 casos totais - segunda maior classe):
Melhor árvore: Excelente performance com 75.0% de acertos (312/416). A confusão principal (24.8%) ocorre com "Híbrido flexível" (103/416), reforçando a sobreposição conceitual entre trabalho remoto e modelos híbridos flexíveis.
Pior árvore: Mantém relativa estabilidade com 68.0% (283/416), perdendo principalmente para "Híbrido flexível" (31.7%). É a classe mais resiliente à degradação da árvore.

Padrões Críticos Identificados
Desbalanceamento extremo de dataset:
A distribuição desproporcional (445 casos de "Híbrido flexível" vs. apenas 21 de "Presencial") cria viés sistemático. O modelo tende a favorecer classes majoritárias, especialmente quando incerto.

Sobreposição conceitual problemática:
A forte confusão entre "Híbrido flexível" e "Modelo 100% remoto" (122 e 271 erros respectivamente) indica que as features coletadas não capturam diferenças fundamentais entre flexibilidade híbrida e trabalho completamente remoto.

Instabilidade arquitetural:
A variação dramática entre melhor (79.8%) e pior árvore (56.7%) revela que o modelo está no limiar da capacidade de generalização. Árvores individuais capturam padrões muito específicos e frágeis dos dados de treino.

### Interpretação do modelo 2

O Modelo 2 utiliza um classificador Random Forest para prever a forma de trabalho ideal dos profissionais. Esse modelo combina diversas árvores de decisão, reduzindo overfitting e aumentando a robustez preditiva.

#### Atributos Mais Relevantes (Feature Importance)
- `P2_r` (Forma de trabalho atual) — maior influência
- `P2_o_4` (Flexibilidade percebida) — importante para distinguir entre remoto e híbrido
- `P2_f` (Cargo atual) — influencia a preferência por modelos mais flexíveis
- `P2_h` (Faixa salarial) — impacto médio

#### Padrões Observados
- Boa performance para prever "Remoto" e "Híbrido flexível".
- A classe "Modelo 100% presencial" teve 0% de acerto, refletindo seu baixo volume no dataset.
- Forte confusão entre "Remoto" e "Híbrido flexível", indicando sobreposição nas características coletadas.

#### Limitações Identificadas
- **Desbalanceamento de classes**: a predominância da classe "Híbrido flexível" afetou negativamente a acurácia nas demais.
- **Similaridade semântica** entre categorias híbridas e remotas dificulta a distinção, mesmo para modelos robustos como o Random Forest.


## Análise comparativa dos modelos

Discuta sobre as forças e fragilidades de cada modelo. Exemplifique casos em que um
modelo se sairia melhor que o outro. Nesta seção é possível utilizar a sua imaginação
e extrapolar um pouco o que os dados sugerem.


### Distribuição do modelo (opcional)

Tende criar um pacote de distribuição para o modelo construído, para ser aplicado 
em um sistema inteligente.


## 8. Conclusão

Apresente aqui a conclusão do seu trabalho. Discussão dos resultados obtidos no trabalho, 
onde se verifica as observações pessoais de cada aluno.

Uma conclusão deve ter 3 partes:

   * Breve resumo do que foi desenvolvido
	 * Apresenação geral dos resultados obtidos com discussão das vantagens e desvantagens do sistema inteligente
	 * Limitações e possibilidades de melhoria




# REFERÊNCIAS

Como um projeto de sistema inteligente não requer revisão bibliográfica, 
a inclusão das referências não é obrigatória. No entanto, caso você 
tenha utilizado referências na introdução ou deseje 
incluir referências relacionadas às tecnologias, padrões, ou metodologias 
que serão usadas no seu trabalho, relacione-as de acordo com a ABNT.

Verifique no link abaixo como devem ser as referências no padrão ABNT:

http://www.pucminas.br/imagedb/documento/DOC\_DSC\_NOME\_ARQUI20160217102425.pdf

Por exemplo:

**[1]** - _ELMASRI, Ramez; NAVATHE, Sham. **Sistemas de banco de dados**. 7. ed. São Paulo: Pearson, c2019. E-book. ISBN 9788543025001._

**[2]** - _COPPIN, Ben. **Inteligência artificial**. Rio de Janeiro, RJ: LTC, c2010. E-book. ISBN 978-85-216-2936-8._

**[3]** - _CORMEN, Thomas H. et al. **Algoritmos: teoria e prática**. Rio de Janeiro, RJ: Elsevier, Campus, c2012. xvi, 926 p. ISBN 9788535236996._

**[4]** - _SUTHERLAND, Jeffrey Victor. **Scrum: a arte de fazer o dobro do trabalho na metade do tempo**. 2. ed. rev. São Paulo, SP: Leya, 2016. 236, [4] p. ISBN 9788544104514._

**[5]** - _RUSSELL, Stuart J.; NORVIG, Peter. **Inteligência artificial**. Rio de Janeiro: Elsevier, c2013. xxi, 988 p. ISBN 9788535237016._



# APÊNDICES

**Colocar link:**

Do código (armazenado no repositório);

Dos artefatos (armazenado do repositório);

Da apresentação final (armazenado no repositório);

Do vídeo de apresentação (armazenado no repositório).
