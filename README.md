# Twitter generate topic dataset

Tool for creating tweet based dataset using the argument.

<img src="https://logos-marcas.com/wp-content/uploads/2020/04/Twitter-Logo.png" height=200 width=350>

# Usage

For upgrading the tool and generate a tweet dataset:
```bash
bash launch.sh keyword1,keyword2,...,keywordN
```

# Example of generated dataset

|id |conversation_id    |created_at         |date           |timezone           |place|tweet|language                                                                                                                                                                                                                                   |hashtags|cashtags|user_id|user_id_str|username  |name      |day |hour|link|urls                                                     |photos|video|thumbnail|retweet                                                                                 |nlikes|nreplies|nretweets|quote_url|search|near|geo|source|user_rt_id|user_rt|retweet_id|reply_to|retweet_date                                                                                     |translate|trans_src|trans_dest|FIELD39|
|---|-------------------|-------------------|---------------|-------------------|-----|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|--------|-------|-----------|----------|----------|----|----|----|---------------------------------------------------------|------|-----|---------|----------------------------------------------------------------------------------------|------|--------|---------|---------|------|----|---|------|----------|-------|----------|--------|-------------------------------------------------------------------------------------------------|---------|---------|----------|-------|
|0  |1429943353995632643|1429906076015767559|1629760037000.0|2021-08-24 01:07:17|+0200|     |@IbaiLand_OOC Sksjssjs                                                                                                                                                                                                                     |sv      |[]      |[]     |2754746065 |2754746065|IbaiLlanos|Ibai|2   |01  |https://twitter.com/IbaiLlanos/status/1429943353995632643|[]    |[]   |0        |                                                                                        |False |3739    |31       |21       |      |None|   |      |          |       |          |        |[{'screen_name': 'IbaiLand_OOC', 'name': 'IbaiLand Out Of Context', 'id': '1221768921272987648'}]|         |         |          |       |
|1  |1429938279722409986|1429938279722409986|1629758827000.0|2021-08-24 00:47:07|+0200|     | https://t.co/ZA5hiwbmuf                                                                                                                                                                                                                   |und     |[]      |[]     |2754746065 |2754746065|IbaiLlanos|Ibai|2   |00  |https://twitter.com/IbaiLlanos/status/1429938279722409986|[]    |[]   |1        |https://pbs.twimg.com/ext_tw_video_thumb/1429938202228498434/pu/img/0vU_X-dKVHoADur6.jpg|False |24064   |225      |1644     |      |None|   |      |          |       |          |        |[]                                                                                               |         |         |          |       |
|2  |1429904134543663106|1429904134543663106|1629750686000.0|2021-08-23 22:31:26|+0200|     | https://t.co/BupGipDyCc                                                                                                                                                                                                                   |und     |[]      |[]     |2754746065 |2754746065|IbaiLlanos|Ibai|1   |22  |https://twitter.com/IbaiLlanos/status/1429904134543663106|[]    |[]   |1        |https://pbs.twimg.com/ext_tw_video_thumb/1429904000745365505/pu/img/3t2QP-evVCrOU1jq.jpg|False |49828   |312      |4591     |      |None|   |      |          |       |          |        |[]                                                                                               |         |         |          |       |
|3  |1429881966552309761|1429881966552309761|1629745401000.0|2021-08-23 21:03:21|+0200|     | https://t.co/FXbGII1Eti                                                                                                                                                                                                                   |und     |[]      |[]     |2754746065 |2754746065|IbaiLlanos|Ibai|1   |21  |https://twitter.com/IbaiLlanos/status/1429881966552309761|[]    |[]   |1        |https://pbs.twimg.com/ext_tw_video_thumb/1425796567127273473/pu/img/bDGOWlYAMIm2rACf.jpg|False |38243   |481      |5006     |      |None|   |      |          |       |          |        |[]                                                                                               |         |         |          |       |
|4  |1429878859504177154|1429878285568299011|1629744660000.0|2021-08-23 20:51:00|+0200|     |@DjMaRiiO unfollow                                                                                                                                                                                                                         |en      |[]      |[]     |2754746065 |2754746065|IbaiLlanos|Ibai|1   |20  |https://twitter.com/IbaiLlanos/status/1429878859504177154|[]    |[]   |0        |                                                                                        |False |17841   |62       |272      |      |None|   |      |          |       |          |        |[{'screen_name': 'DjMaRiiO', 'name': 'Fabrizio Romano', 'id': '202535200'}]                      |         |         |          |       |
|5  |1429822295720267782|1429822295720267782|1629731174000.0|2021-08-23 17:06:14|+0200|     |Tomad este clip como ejemplo de actitud en la vida  https://t.co/DsF5G0s7dw                                                                                                                                                                |es      |[]      |[]     |2754746065 |2754746065|IbaiLlanos|Ibai|1   |17  |https://twitter.com/IbaiLlanos/status/1429822295720267782|[]    |[]   |1        |https://pbs.twimg.com/ext_tw_video_thumb/1429817188865740817/pu/img/xHhYCIexIgE_x6XF.jpg|False |38373   |192      |2180     |      |None|   |      |          |       |          |        |[]                                                                                               |         |         |          |       |
|6  |1429707452015071234|1429706177282195458|1629703793000.0|2021-08-23 09:29:53|+0200|     |@iPandarina por favor respeta                                                                                                                                                                                                              |es      |[]      |[]     |2754746065 |2754746065|IbaiLlanos|Ibai|1   |09  |https://twitter.com/IbaiLlanos/status/1429707452015071234|[]    |[]   |0        |                                                                                        |False |3277    |31       |29       |      |None|   |      |          |       |          |        |[{'screen_name': 'iPandarina', 'name': 'Pandarina González Paredes', 'id': '414958974'}]         |         |         |          |       |
|7  |1429598828668325889|1429532479862493190|1629677896000.0|2021-08-23 02:18:16|+0200|     |@CarlosR Sois la hostia. Y Fnatic también. Los dos únicos equipos que me hacen vivir el LoL como en 2015. Puedes estar orgulloso de todo lo que has conseguido, Carlos. Alguna vez tendrías que perder cabrón.                             |es      |[]      |[]     |2754746065 |2754746065|IbaiLlanos|Ibai|1   |02  |https://twitter.com/IbaiLlanos/status/1429598828668325889|[]    |[]   |0        |                                                                                        |False |5181    |17       |112      |      |None|   |      |          |       |          |        |[{'screen_name': 'CarlosR', 'name': 'CarlosR ocelote', 'id': '320349454'}]                       |         |         |          |       |
|8  |1429563119785943046|1429562929159053324|1629669382000.0|2021-08-22 23:56:22|+0200|     |@finallyxpablo Cabron que se ha puesto en la portería en el 89 y se han jugado 3 minutos sjsjask                                                                                                                                           |es      |[]      |[]     |2754746065 |2754746065|IbaiLlanos|Ibai|7   |23  |https://twitter.com/IbaiLlanos/status/1429563119785943046|[]    |[]   |0        |                                                                                        |False |411     |22       |9        |      |None|   |      |          |       |          |        |[{'screen_name': 'finallyxpablo', 'name': '🅿', 'id': '851377745309429765'}]                     |         |         |          |       |
|9  |1429560848373137410|1429560848373137410|1629668840000.0|2021-08-22 23:47:20|+0200|     |Vinicius en dos partidos saliendo desde el banquillo ha marcado tres goles y ha forzado la expulsión del portero del Levante que va a tener que jugar con un jugador de campo de portero. Os juro que siento que estoy totalmente borracho.|es      |[]      |[]     |2754746065 |2754746065|IbaiLlanos|Ibai|7   |23  |https://twitter.com/IbaiLlanos/status/1429560848373137410|[]    |[]   |0        |                                                                                        |False |36298   |328      |1785     |      |None|   |      |          |       |          |        |[]                                                                                               |         |         |          |       |
|10 |1429559884589281281|1429559884589281281|1629668611000.0|2021-08-22 23:43:31|+0200|     |ESTOY FLIPANDO CON VINICIUS   ES PELÉ                                                                                                                                                                                                      |es      |[]      |[]     |2754746065 |2754746065|IbaiLlanos|Ibai|7   |23  |https://twitter.com/IbaiLlanos/status/1429559884589281281|[]    |[]   |0        |                                                                                        |False |69838   |938      |3771     |      |None|   |      |          |       |          |        |[]                                                                                               |         |         |          |       |
