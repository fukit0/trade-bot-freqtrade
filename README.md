# Auto Trading Bot

## Prerequisites
1. Install [Docker](https://docs.docker.com/engine/install/ubuntu/)
2. Install [Docker-compose](https://docs.docker.com/compose/install/)
3. Clone project.
4. For linux, change project folder permission;
```sh
$ sudo chmod -R 777 `<PROJECT_FOLDER>`
```

## Dry-Run or Live-Trading

After all changes in project folder, you should add `--build` to command

```sh
$ docker-compose up -d --build
```

## Data Downloading

Getting data for backtesting and hyperopt

```sh
$ docker-compose run --rm freqtrade download-data --erase -t 5m --timerange 20210101-20210515
```

## Backtesting

- Generic Command

```sh
$ docker-compose run --rm freqtrade backtesting --strategy-list BBRSI --timeframe 5m --export trades --export-filename=user_data/backtest_results/BBRSI_result.json

$ docker-compose run --rm freqtrade backtesting --strategy-list ONUR YABAR YABAR2 --timeframe 5m --export trades --export-filename=user_data/backtest_results/YABAR_onur_yabar2_result.json --timerange 20210101-20210515
```
20210414-20210427
```
freqtrade backtesting --timerange 20180401-20180410 --timeframe 5m --strategy-list Strategy001 Strategy002 --export trades

```
- Command example

```sh
$ docker-compose run --rm freqtrade backtesting --strategy-list BBRSI --timeframe 15m --export trades --export-filename=user_data/backtest_results/BBRSI_result.json
```


## Hyperopt

- Generic Command

```sh
$ docker-compose run --rm freqtrade hyperopt --hyperopt `<HYPEROPTNAME>` --hyperopt-loss `<HYPEROPTLOSSNAME>` --strategy `<STRATEGY>` -e `<EVALUATION_COUNT>`
```

- Command example

```sh
$ docker-compose run --rm freqtrade hyperopt --hyperopt SampleHyperOpt --hyperopt-loss SampleHyperOptLoss --strategy BBRSI -e 10
```

## plotting
```
dcr freqtrade plot-dataframe --strategy BBRSI -p DOGE/USDT i- 15m
```


## troubleshooting

`docker logs -f --tail 100 container-id` to see logs

`docker container rm -f name` to remove container
