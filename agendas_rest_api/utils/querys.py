
# TOTAL DE VAGAS APLICATIVO
def getQueryVagasApp():
    queryVagasApp = 'WITH total_dermato AS ( SELECT '
    queryVagasApp = queryVagasApp + "C.NM_FANTASIA_ESTAB AS ESTABELECIMENTO, "
    queryVagasApp = queryVagasApp + "OBTER_NOME_MEDICO(B.CD_PESSOA_FISICA,'N') AS PROFISSIONAL, "
    queryVagasApp = queryVagasApp + "OBTER_DESC_ESPEC_MEDICA(B.CD_ESPECIALIDADE) AS ESPECIALIDADE, "
    queryVagasApp = queryVagasApp + "COUNT(A.IE_STATUS_AGENDA) AS QUANTIDADE_DE_VAGAS "
    queryVagasApp = queryVagasApp + "from AGENDA_CONSULTA A "
    queryVagasApp = queryVagasApp + "INNER JOIN AGENDA B ON (A.CD_AGENDA = B.CD_AGENDA) "
    queryVagasApp = queryVagasApp + "INNER JOIN ESTABELECIMENTO C ON (B.CD_ESTABELECIMENTO = C.CD_ESTABELECIMENTO) "
    queryVagasApp = queryVagasApp + "INNER JOIN AGENDA_TURNO D ON (B.CD_AGENDA = D.CD_AGENDA AND A.NR_SEQ_TURNO = D.NR_SEQUENCIA) "
    queryVagasApp = queryVagasApp + "WHERE "
    queryVagasApp = queryVagasApp + "A.IE_STATUS_AGENDA = 'L' "
    queryVagasApp = queryVagasApp + "AND B.CD_ESPECIALIDADE IN(49) "                              # A CONSULTA FOI ALTERADA AQUI. FORMA ADICIONADOS NOVOS CÓDIGOS DE ESPECIALIDADE
    queryVagasApp = queryVagasApp + "AND C.CD_ESTABELECIMENTO <> '22' "
    queryVagasApp = queryVagasApp + "AND A.DT_AGENDA BETWEEN SYSDATE AND (SYSDATE+10) "
    queryVagasApp = queryVagasApp + "AND D.DS_OBS_INTERNA LIKE '%@CST@%' "
    queryVagasApp = queryVagasApp + "GROUP BY C.NM_FANTASIA_ESTAB, OBTER_NOME_MEDICO(B.CD_PESSOA_FISICA,'N'), OBTER_DESC_ESPEC_MEDICA(B.CD_ESPECIALIDADE) "
    queryVagasApp = queryVagasApp + "ORDER BY COUNT(A.IE_STATUS_AGENDA) DESC, C.NM_FANTASIA_ESTAB, OBTER_NOME_MEDICO(B.CD_PESSOA_FISICA,'N'), OBTER_DESC_ESPEC_MEDICA(B.CD_ESPECIALIDADE) "
    queryVagasApp = queryVagasApp + "), "
    queryVagasApp = queryVagasApp + "total_ped AS ( "
    queryVagasApp = queryVagasApp + "select "
    queryVagasApp = queryVagasApp + "C.NM_FANTASIA_ESTAB AS ESTABELECIMENTO, "
    queryVagasApp = queryVagasApp + "OBTER_NOME_MEDICO(B.CD_PESSOA_FISICA,'N') AS PROFISSIONAL, "
    queryVagasApp = queryVagasApp + "OBTER_DESC_ESPEC_MEDICA(B.CD_ESPECIALIDADE) AS ESPECIALIDADE, "
    queryVagasApp = queryVagasApp + "COUNT(A.IE_STATUS_AGENDA) AS QUANTIDADE_DE_VAGAS "
    queryVagasApp = queryVagasApp + "from AGENDA_CONSULTA A "
    queryVagasApp = queryVagasApp + "INNER JOIN AGENDA B ON (A.CD_AGENDA = B.CD_AGENDA) " 
    queryVagasApp = queryVagasApp + "INNER JOIN ESTABELECIMENTO C ON (B.CD_ESTABELECIMENTO = C.CD_ESTABELECIMENTO) "
    queryVagasApp = queryVagasApp + "INNER JOIN AGENDA_TURNO D ON (B.CD_AGENDA = D.CD_AGENDA AND A.NR_SEQ_TURNO = D.NR_SEQUENCIA) "
    queryVagasApp = queryVagasApp + "WHERE A.IE_STATUS_AGENDA = 'L' " 
    queryVagasApp = queryVagasApp + "AND B.CD_ESPECIALIDADE IN(3) "
    queryVagasApp = queryVagasApp + "AND C.CD_ESTABELECIMENTO <> '22' " 
    queryVagasApp = queryVagasApp + "AND A.DT_AGENDA BETWEEN SYSDATE AND (SYSDATE+6) "
    queryVagasApp = queryVagasApp + "AND D.DS_OBS_INTERNA LIKE '%@CST@%' "
    queryVagasApp = queryVagasApp + "GROUP BY C.NM_FANTASIA_ESTAB, OBTER_NOME_MEDICO(B.CD_PESSOA_FISICA,'N'), OBTER_DESC_ESPEC_MEDICA(B.CD_ESPECIALIDADE) " 
    queryVagasApp = queryVagasApp + "ORDER BY COUNT(A.IE_STATUS_AGENDA) DESC, C.NM_FANTASIA_ESTAB, OBTER_NOME_MEDICO(B.CD_PESSOA_FISICA,'N'), OBTER_DESC_ESPEC_MEDICA(B.CD_ESPECIALIDADE) )" 
    queryVagasApp = queryVagasApp + "SELECT * FROM ("
    queryVagasApp = queryVagasApp + "SELECT ESPECIALIDADE, SUM(QUANTIDADE_DE_VAGAS) AS QTD FROM total_dermato GROUP BY ESPECIALIDADE " 
    queryVagasApp = queryVagasApp + "UNION SELECT ESPECIALIDADE, SUM(QUANTIDADE_DE_VAGAS) AS QTD FROM total_ped GROUP BY ESPECIALIDADE " 
    queryVagasApp = queryVagasApp + ")ORDER BY QTD"
    return queryVagasApp





def getQueryAgendamentosRealizados(especialidade, dataInicio, dataFim):
    agendamentosApp = "select "
    agendamentosApp = agendamentosApp + "OBTER_DESC_ESPEC_MEDICA(B.CD_ESPECIALIDADE) AS ESPECIALIDADE, "
    agendamentosApp = agendamentosApp + "to_char(A.DT_AGENDA, 'dd/mm/yyyy'), "
    agendamentosApp = agendamentosApp + "COUNT(A.IE_STATUS_AGENDA) AS QUANTIDADE_DE_VAGAS "
    agendamentosApp = agendamentosApp + "from AGENDA_CONSULTA A "
    agendamentosApp = agendamentosApp + "INNER JOIN AGENDA B ON (A.CD_AGENDA = B.CD_AGENDA) "
    agendamentosApp = agendamentosApp + "INNER JOIN ESTABELECIMENTO C ON (B.CD_ESTABELECIMENTO = C.CD_ESTABELECIMENTO) "
    agendamentosApp = agendamentosApp + "INNER JOIN AGENDA_TURNO D ON (B.CD_AGENDA = D.CD_AGENDA AND A.NR_SEQ_TURNO = D.NR_SEQUENCIA) "
    agendamentosApp = agendamentosApp + " AND B.CD_ESPECIALIDADE IN('"+ especialidade +"') "
    agendamentosApp = agendamentosApp + "AND C.CD_ESTABELECIMENTO <> '22' "
    agendamentosApp = agendamentosApp + "AND A.DT_AGENDA BETWEEN to_date('" + dataInicio + "','dd/mm/yyyy') AND to_date('" + dataFim + "','dd/mm/yyyy') "
    agendamentosApp = agendamentosApp + "AND B.IE_SITUACAO = 'A' "
    agendamentosApp = agendamentosApp + "GROUP BY OBTER_DESC_ESPEC_MEDICA(B.CD_ESPECIALIDADE), to_char(A.DT_AGENDA, 'dd/mm/yyyy') "
    agendamentosApp = agendamentosApp + "order by OBTER_DESC_ESPEC_MEDICA(B.CD_ESPECIALIDADE), to_char(A.DT_AGENDA, 'dd/mm/yyyy')"
    return agendamentosApp



        
        
        
        
        
        
        
        