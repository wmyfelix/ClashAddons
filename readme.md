```
for learning purpose.
```
currently work as a part of [subconverter](https://github.com/tindy2013/subconverter).
# Usage
define config path in `smart.py` then run it.
## Configuration
```yaml
# omc/config-sample.yaml
Enabled: <Bool>
Output Dir: <dir>
Git:
  email: 
  name: 
SCServer: 127.0.0.1:25500
SCServerRemote: api.wcc.best # remote subconverter server for quanx config.
Storage: <url> # where proxies store.
ProxyProviders:
#  <name1>: <url1>
#  <name2>: <url2>
# ...
ClashProviders:
  target: clash
  # belows are args provided to subconverter.
  list: true
  udp: true
  emoji: true
  sort: true
  #
QuantumultXRemotes: 
  target: quanx
  list: true
#ExcludeExp: # not a must-leave field.
#  syntax: 奈飞小铺|过期时间|剩余流量|官网|机场|维护 # regular expression that is given to subsconverter.
#  whitelist: 
#  - <provider1>
#  - <provider2>
#  ...
QuickGenQX: true # generate config by subconverter with its template.
SmartFilter: 
## Examples:
#  provider1: \d*\.*\d+(?:x|X|倍|倍率)
#  provider2: \d*\.*\d+(?:x|X|倍|倍率)|限速|Game|游戏|原生|IEPL|IPLC
##
Rules:
  Clash:
  # belows could be url(http/https) or file path on the system. 
    head: template/clash/head.yml
    rules: template/clash/connershua/rules.yml 
```