# smokescreen
Flood a cloudflare/WAF server with thousands of fake traffic and security logs

![](https://i.ibb.co/v3CYfpQ/smokescreenbanner.png)

## How it works

This tool uses many frequently updated lists of open source proxies and user agent spoofing methods to flood a victims server logs or WAF with deceiving or overwhelming false traffic logs and events ***NOT*** to DDOS.

Each flagged request comes with its own unique and anonymous IP address and randomly generated user agent, allowing an attacker to ***"blend in amongs the noise"*** and obfuscate themself in the fake traffic created.

![](https://i.ibb.co/PT5KTh0/In-Shot-20230905-195343771.jpg)

The requests sent out are purposely designed to cause red flags and be seen within a victims firewall, in order to mask and/or obfuscate potentially other malicious traffic an attacker may send, it does this by sending the HTTP/1.1 requests within irregular methods or traffic spikes, not enough to cause a DDOS- but enough to hide other activities that the firewall may be flagging at the time or current "***under the radar***" DDOS attacks.

![](https://i.ibb.co/4YQXJbJ/events.png)

## Purpose

This tool is useful for firewall testing and obfuscation/bypass purposes- along with the use to hide current payloads or attacks sent to a web server.

It can essentialy "***Jam***" or create noise in almost any web-facing HTTP based firewalls and words more than well against ***Cloudflare's*** WAF and "***Event***" catcher.

![](https://i.ibb.co/021wBcw/events2.png)

## Impact/Disclaimer

Although this tool is capable of sending thousands of false requests a minute from individually unique IP addresses and user agents, it is not designed for the purposes of performing a "***Denial Of Service Attack***" It still may coincidentally perform one, so be careful.

![](https://i.ibb.co/98cwZVZ/no2.png)


## Install

To use this tool you must have ***python3.9+*** with ***pip3+*** or similar package installer.

With the following libaries:

Colorama - (https://pypi.org/project/colorama/)

Requests - (https://pypi.org/project/requests/)

Faker - (https://pypi.org/project/Faker/)

