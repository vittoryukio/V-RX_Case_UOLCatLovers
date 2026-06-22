EXPORT DATA OPTIONS(
  uri='gs://DW_CATFACTS/AMOSTRA_100_FATOS_GATOS_ALEATORIA.csv',
  format='CSV',
  overwrite=true,
  header=true,
  field_delimiter=','
) AS
SELECT 
    DS_TEXT_FACTS,
    DT_CREATED_AT,
    DT_LAST_UPDATE
FROM 
    DW_CATFACTS.TB_CAT_FACTS
ORDER BY 
    RAND()
LIMIT 100;