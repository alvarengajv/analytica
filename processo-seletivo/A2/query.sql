SELECT
ano,
bd.sigla_uf,
bd.id_municipio,
indice_sem_atendimento_sem_coleta_sem_tratamento,
indice_atendimento_com_coleta_sem_tratamento,
indice_atendimento_com_coleta_com_tratamento,
sum(investimento_tratamento) as inv_tratamento,
sum(investimento_coleta) as inv_coleta,
sum(investimento_coleta_tratatamento) as inv_col_tratamento,
sum(populacao_urbana_2013) as pop_2013,
sum(populacao_urbana_2035) as pop_2035,
round((sum(populacao_urbana_2035)/sum(populacao_urbana_2013)-1),2) as delta_pop,
sum(populacao_atendida_2035) as pop_esperada_2035,
sum(total) as total_transp,
sum(automovel) as automovel,
sum(automovel)/sum(total) perc_auto,
sum(motocicleta) as moto,
sum(microonibus) as micro_onibus,
sum(onibus) as onibus
FROM `basedosdados.br_denatran_frota.municipio_tipo` as bd
left join `basedosdados.br_ana_atlas_esgotos.municipio` as ba on ba.id_municipio = bd.id_municipio
where ano = 2013
and mes = 12
group by 1,2,3,4,5,6
order by 10 desc
