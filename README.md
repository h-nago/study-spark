# 概要
Sparkクラスターお試し。

# データ作成
行数を指定して単語数カウント用データを作成する
```
docker-compose run --rm spark-master python3 /app/create-data-for-wordcount.py <record count> > <file name>
```
行数を指定して平均計算用データを作成する
```
docker-compose run --rm spark-master python3 /app/create-data-for-wordcount.py <record count> > <file name>
```

# Spark Cluster起動
```
docker-compose up -d --scale spark-slave=<起動したいslaveの数>
```

# 計算を実行
単語数カウント
```
docker-compose exec spark-master bash -c "source /root/.bashrc && python3 /app/wordcount.py <DataFileName>"
```

平均計算
```
docker-compose exec spark-master bash -c "source /root/.bashrc && python3 /app/average.py <DataFileName>"
```

# 結果
単語数カウント(10000行)

| worker数 | 実行時間(s) |
| - | - |
| 1 | 50 |  
| 2 | 35 |
| 3 | 30 |

平均計算(10000行)

| worker数 | 実行時間(s) |
| - | - |
| 1 | 27 |  
| 2 | 30 |
| 3 | 30 |

# 考察
平均計算ではワーカーを増やすと処理時間が増えた。CPU負荷が小さい処理だと、ワーカー間通信分時間が余計にかかるということ？
saveAsTextFileした後は、Executorごとに処理結果が出力されるらしいが、平均計算の場合は200個ファイルがあった（単語数カウントは2個）。うまく分散されておらず、無駄な処理が発生している気がする。