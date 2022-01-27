既然这个仓库被发现了，我也有做些说明的必要了。  
这是我用于对来自多个提供商的订阅节点进行整合，分类，并生成订阅文件的脚本。  
由于我蒟蒻，所以一度只得将订阅文件托管在公开的仓库中。  
于是，我的上网体验在这个仓库被注意到后受到了影响，但**这个仓库本意不是分享节点**。  
现在我将原库改为私有，使用 Cloudflare Pages 托管生成的订阅文件，并将本库改为 Template 库 ，解决了暴露节点甚至违反供应商服务条款的问题。

lhie1的规则库似乎被Github关闭了，可使用ConnersHua规则。

我的目标是将该脚本部署在 cloudflare worker 上，但缺乏 javascript 和 http request 相关知识，再加上我的生活状态之差，实现该目标遥遥无期。

----
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