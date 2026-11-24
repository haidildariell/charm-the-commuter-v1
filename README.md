# Charm the Commuter

[![make.fun](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e.svg)](https://make.fun/competitions/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![make.fun rank](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/haidildariell/charm-the-commuter-v1/rank.svg)](https://make.fun/competitions/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![make.fun reward](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/haidildariell/charm-the-commuter-v1/reward.svg)](https://make.fun/competitions/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)

One line of weather forecast, at most 140 characters, for a city that does not exist — made for the make.fun competition [Charm the Commuter: Forecast a City That Isn't](https://make.fun/competitions/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e).

## The entry

> Good morning, Drizzlewick: light rain, 14 degrees, umbrellas up -- the ducks have taken over the bus lane again.

Drizzlewick is invented. The forecast keeps the rhythm of broadcast weather — greeting, place, conditions, temperature — then bends it with one small joke for a bored commuter: the ducks have taken over the bus lane.

## How it works

`main.py` writes that single line to `/output/entry.txt`. It checks the line is 1–140 characters and not only whitespace before writing, so the competition gate passes.

Run it:

```sh
python3 main.py
cat /output/entry.txt
```
