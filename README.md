# frequency-analysis

This projects decodes the input string and calculates the chi-squared score of the decoded string.
The lower the score, the more likely you have the decoded output is in the target language.

## Project setup

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Commands

```
python src/main.py       run the project (only pipe input is supported)
pytest                   run unit tests
ptw                      run unit tests in watch mode
pytest --cov=src src/    run unit tests and display test coverage
```

## Examples

```
echo "aoljhlzhyjpwolypzvulvmaollhysplzaruvduhukzptwslzajpwolyzpapzhafwlvmzbizapabapvujpwolypudopjolhjoslaalypuaolwshpualeapzzopmalkhjlyahpuubtilyvmwshjlzkvduaolhswohila" | python src/main.py | sort -t ":" -n -b +3
```

output:

```
source:  aoljhlzhyjpwolypzvulvmaollhysplzaruvduhukzptwslzajpwolyzpapzhafwlvmzbizapabapvujpwolypudopjolhjoslaalypuaolwshpualeapzzopmalkhjlyahpuubtilyvmwshjlzkvduaolhswohila
rot: 19 output: thecaesarcipher | score:      25.34
rot:  6 output: gurpnrfnepvcure | score:     429.20
rot:  4 output: espnlpdlcntaspc | score:     676.78
rot: 13 output: nbywuymulwcjbyl | score:     720.91
rot: 15 output: pdaywaownyeldan | score:     785.14
rot:  7 output: hvsqosgofqwdvsf | score:     922.03
rot: 22 output: wkhfdhvduflskhu | score:    1167.62
rot:  3 output: dromkockbmszrob | score:    1207.78
rot: 17 output: rfcaycqypagnfcp | score:    1326.14
rot:  8 output: iwtrpthpgrxewtg | score:    1342.50
rot: 21 output: vjgecguctekrjgt | score:    1430.35
rot: 23 output: xligeiwevgmtliv | score:    1522.75
rot:  0 output: aoljhlzhyjpwoly | score:    1612.04
rot: 18 output: sgdbzdrzqbhogdq | score:    1734.29
rot: 11 output: lzwuswksjuahzwj | score:    1744.18
rot: 20 output: uifdbftbsdjqifs | score:    1780.35
rot:  2 output: cqnljnbjalryqna | score:    1808.46
rot: 12 output: maxvtxltkvbiaxk | score:    2209.91
rot: 24 output: ymjhfjxfwhnumjw | score:    2916.68
rot:  9 output: jxusquiqhsyfxuh | score:    2955.64
rot:  1 output: bpmkimaizkqxpmz | score:    2985.19
rot: 25 output: znkigkygxiovnkx | score:    3418.71
rot: 10 output: kyvtrvjritzgyvi | score:    3494.51
rot: 16 output: qebzxbpxozfmebo | score:    3522.77
rot:  5 output: ftqomqemdoubtqd | score:    4375.85
rot: 14 output: oczxvznvmxdkczm | score:    4607.28
```

## Roadmap

- add multi-lines support
- add input file flag support
- add uppercase support
- add other decoding cyphers algorythms
