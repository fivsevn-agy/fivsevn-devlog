# Intake Sources

> Canonical hand-maintained source registry for the intake page.
>
> Edit this file, then run `python intake/build.py` to regenerate `feeds.yml` and the final page.

## 目录 / First & Second Level Catalog

- [世界 / world](#world)
  - [媒介透镜 / media_lens](#media_lens)
  - [世界与社会 / world_society](#world_society)
- [经济 / economy](#economy)
  - [价格与市场 / prices_markets](#prices_markets)
  - [能源与资源 / energy_resources](#energy_resources)
  - [食物与农业市场 / food_agriculture_markets](#food_agriculture_markets)
  - [居住与生活成本 / housing_living_costs](#housing_living_costs)
  - [供应链与贸易 / supply_chains_trade](#supply_chains_trade)
  - [产业与商业 / industry_business](#industry_business)
  - [货币与金融 / money_finance](#money_finance)
- [观念 / ideas](#ideas)
  - [公共观念 / public_ideas](#public_ideas)
  - [学术观念 / scholarly_ideas](#scholarly_ideas)
  - [文明批评 / civilizational_critique](#civilizational_critique)
- [文化形式 / cultural_forms](#cultural_forms)
  - [书籍 / books](#books)
  - [电影与影像 / film_moving_image](#film_moving_image)
  - [音乐与声音 / music_sound](#music_sound)
  - [摄影 / photography](#photography)
  - [艺术与设计 / arts_design](#arts_design)
  - [建筑与城市 / architecture_urbanism](#architecture_urbanism)
  - [游戏与科幻 / games](#games)
  - [时尚与风格 / fashion_style](#fashion_style)
- [人类研究 / human_studies](#human_studies)
  - [人类社会 / human_societies](#human_societies)
  - [心智 / mind](#mind)
- [自然 / nature](#nature)
  - [科学新闻 / science_news](#science_news)
  - [科普杂志 / science_magazines](#science_magazines)
  - [学术研究 / research](#research)
  - [航天与宇宙 / space_astronomy](#space_astronomy)
  - [自然史 / natural_history](#natural_history)
  - [生态与保护 / ecology_conservation](#ecology_conservation)
  - [动物行为 / animal_behavior](#animal_behavior)
  - [海洋生命 / marine_life](#marine_life)
  - [鱼类与鱼类学 / fish_ichthyology](#fish_ichthyology)
  - [贝壳与软体动物 / mollusks](#mollusks)
  - [节肢动物 / arthropods](#arthropods)
  - [植物与真菌 / plants_fungi](#plants_fungi)
  - [矿物与地质 / minerals_geology](#minerals_geology)
- [技术 / technology](#technology)
  - [AI 系统 / ai_systems](#ai_systems)
  - [计算文化 / computing_cultures](#computing_cultures)
  - [平台与基础设施 / platforms_infrastructure](#platforms_infrastructure)
  - [界面与媒介技术 / interfaces_media_technology](#interfaces_media_technology)
  - [控制论与自动化 / cybernetics_automation](#cybernetics_automation)
  - [硬件、无线电与嵌入式 / hardware_radio_embedded](#hardware_radio_embedded)
  - [业余无线电 / ham_radio](#ham_radio)
  - [技术政治 / technology_politics](#technology_politics)
- [器物 / material](#material)
  - [野外装备 / field_gear](#field_gear)
  - [日用携行 / everyday_carry](#everyday_carry)
  - [工具与工坊 / tools_workshop](#tools_workshop)
  - [维修与维护 / repair_maintenance](#repair_maintenance)
  - [手册 / manuals](#manuals)
- [参考 / reference](#reference)
  - [参考来源暂存 / reference_pool](#reference_pool)
  - [地图与地理数据 / maps_geo_data](#maps_geo_data)
  - [文档检索 / document_search](#document_search)
  - [RSS 与信息管理 / rss_feed_management](#rss_feed_management)
  - [档案与聚合 / archives_aggregators](#archives_aggregators)
  - [社区与讨论 / communities_discussion](#communities_discussion)

```categories
world:
  title: world
  title_zh: 世界
  sections:
  - media_lens
  - world_society
economy:
  title: economy
  title_zh: 经济
  sections:
  - prices_markets
  - energy_resources
  - food_agriculture_markets
  - housing_living_costs
  - supply_chains_trade
  - industry_business
  - money_finance
ideas:
  title: ideas
  title_zh: 观念
  sections:
  - public_ideas
  - scholarly_ideas
  - civilizational_critique
cultural_forms:
  title: cultural_forms
  title_zh: 文化形式
  sections:
  - books
  - film_moving_image
  - music_sound
  - photography
  - arts_design
  - architecture_urbanism
  - games
  - fashion_style
human_studies:
  title: human_studies
  title_zh: 人类研究
  sections:
  - human_societies
  - mind
nature:
  title: nature
  title_zh: 自然
  sections:
  - science_news
  - science_magazines
  - research
  - space_astronomy
  - natural_history
  - ecology_conservation
  - animal_behavior
  - marine_life
  - fish_ichthyology
  - mollusks
  - arthropods
  - plants_fungi
  - minerals_geology
technology:
  title: technology
  title_zh: 技术
  sections:
  - ai_systems
  - computing_cultures
  - platforms_infrastructure
  - interfaces_media_technology
  - cybernetics_automation
  - hardware_radio_embedded
  - ham_radio
  - technology_politics
material:
  title: material
  title_zh: 器物
  sections:
  - field_gear
  - everyday_carry
  - tools_workshop
  - repair_maintenance
  - manuals
reference:
  title: reference
  title_zh: 参考
  sections:
  - reference_pool
  - maps_geo_data
  - document_search
  - rss_feed_management
  - archives_aggregators
  - communities_discussion
```


<a id="world"></a>

# 世界 / world

<a id="media_lens"></a>

## 媒介透镜 / media_lens

```section
id: media_lens
title: media lens
title_zh: 媒介透镜
description_zh: ''
```

```source
name: Google News
section: media_lens
feed_url: ''
source_cap: 0
site_url: https://news.google.com/
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

```source
name: Yahoo News
section: media_lens
feed_url: ''
source_cap: 0
site_url: https://news.yahoo.com/
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

```source
name: NewsNow
section: media_lens
feed_url: ''
source_cap: 0
site_url: https://www.newsnow.co.uk/
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

```source
name: News Now
section: media_lens
feed_url: ''
source_cap: 0
site_url: https://newsnow.busiyi.world
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

```source
name: Real Time
section: media_lens
feed_url: ''
source_cap: 0
site_url: http://realtime.info
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

```source
name: Buzzing
section: media_lens
feed_url: ''
source_cap: 0
site_url: https://www.buzzing.cc
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

```source
name: 嘎!RSS
section: media_lens
feed_url: ''
source_cap: 0
site_url: https://zhaoolee.com/garss/#/
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

```source
name: 今日热榜
section: media_lens
feed_url: ''
source_cap: 0
site_url: https://tophub.today
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

```source
name: Ground News
section: media_lens
feed_url: ''
source_cap: 0
site_url: https://ground.news/
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

```source
name: AllSides
section: media_lens
feed_url: ''
source_cap: 0
site_url: https://www.allsides.com/
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

```source
name: Ad Fontes Media
section: media_lens
feed_url: ''
source_cap: 0
site_url: https://adfontesmedia.com/
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

```source
name: The Flip Side
section: media_lens
feed_url: ''
source_cap: 0
site_url: https://www.theflipside.io/
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

```source
name: Tangle
section: media_lens
feed_url: ''
source_cap: 0
site_url: https://www.readtangle.com/
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

```source
name: Verity / Improve the News
section: media_lens
feed_url: ''
source_cap: 0
site_url: https://www.improvethenews.org/
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

```source
name: Biasly
section: media_lens
feed_url: ''
source_cap: 0
site_url: https://www.biasly.com/
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

```source
name: SmartNews
section: media_lens
feed_url: ''
source_cap: 0
site_url: https://www.smartnews.com/en
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

```source
name: Mediagazer
section: media_lens
feed_url: https://www.mediagazer.com/feed.xml
source_cap: 6
site_url: https://www.mediagazer.com/
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

```source
name: Nieman Journalism Lab
section: media_lens
feed_url: https://www.niemanlab.org/feed/
source_cap: 6
site_url: https://www.niemanlab.org/
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

```source
name: Nieman Reports
section: media_lens
feed_url: https://niemanreports.org/feed/
source_cap: 6
site_url: https://niemanreports.org/
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

```source
name: EuroTopics
section: media_lens
feed_url: ''
source_cap: 0
site_url: https://www.eurotopics.net/
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

```source
name: World News Map
section: media_lens
feed_url: ''
source_cap: 0
site_url: https://www.map.news/
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```


```source
name: Columbia Journalism Review
section: media_lens
feed_url: https://www.cjr.org/feed
source_cap: 6
site_url: https://www.cjr.org/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 5
use_role: reference
```

```source
name: Poynter
section: media_lens
feed_url: https://www.poynter.org/feed/
source_cap: 6
site_url: https://www.poynter.org/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 5
use_role: reference
```

```source
name: Press Gazette
section: media_lens
feed_url: https://pressgazette.co.uk/feed/
source_cap: 6
site_url: https://pressgazette.co.uk/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: reference
```

```source
name: Journalism.co.uk
section: media_lens
feed_url: https://www.journalism.co.uk/rss/1/s2/
source_cap: 6
site_url: https://www.journalism.co.uk/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: reference
```

<a id="world_society"></a>

## 世界与社会 / world_society

```section
id: world_society
title: world society
title_zh: 世界与社会
description_zh: ''
```

```source
name: Reuters
section: world_society
feed_url: https://www.reuters.com/arc/outboundfeeds/rss/?outputType=xml
source_cap: 6
site_url: https://www.reuters.com/
source_type: wire_service
authority_level: generalist
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: Reuters World
section: world_society
feed_url: https://www.reuters.com/arc/outboundfeeds/rss/category/world/?outputType=xml
source_cap: 6
site_url: https://www.reuters.com/world/
source_type: wire_service
authority_level: generalist
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: Reuters U.S.
section: world_society
feed_url: https://www.reuters.com/arc/outboundfeeds/rss/category/world/us/?outputType=xml
source_cap: 6
site_url: https://www.reuters.com/world/us/
source_type: wire_service
authority_level: generalist
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: Associated Press / AP
section: world_society
feed_url: https://apnews.com/hub/ap-top-news?output=rss
source_cap: 6
site_url: https://apnews.com/
source_type: wire_service
authority_level: generalist
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: AP World
section: world_society
feed_url: https://apnews.com/hub/world-news?output=rss
source_cap: 6
site_url: https://apnews.com/hub/world-news
source_type: wire_service
authority_level: generalist
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: AP U.S. News
section: world_society
feed_url: https://apnews.com/hub/us-news?output=rss
source_cap: 6
site_url: https://apnews.com/hub/us-news
source_type: wire_service
authority_level: generalist
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: Agence France-Presse / AFP
section: world_society
feed_url: ''
source_cap: 0
site_url: https://www.afp.com/
source_type: wire_service
authority_level: generalist
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: DPA 德新社
section: world_society
feed_url: ''
source_cap: 0
site_url: https://www.dpa.com/
source_type: wire_service
authority_level: generalist
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: Kyodo 共同通信
section: world_society
feed_url: ''
source_cap: 0
site_url: https://english.kyodonews.net/
source_type: wire_service
authority_level: generalist
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: Jiji Press 时事通信社
section: world_society
feed_url: ''
source_cap: 0
site_url: https://www.jiji.com/
source_type: wire_service
authority_level: generalist
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: TASS 塔斯社
section: world_society
feed_url: ''
source_cap: 0
site_url: https://tass.com/
source_type: wire_service
authority_level: generalist
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: Xinhua 新华社
section: world_society
feed_url: ''
source_cap: 0
site_url: http://www.xinhuanet.com/english/
source_type: wire_service
authority_level: generalist
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: EFE
section: world_society
feed_url: ''
source_cap: 0
site_url: https://efe.com/
source_type: wire_service
authority_level: generalist
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: ANSA
section: world_society
feed_url: ''
source_cap: 0
site_url: https://www.ansa.it/english/
source_type: wire_service
authority_level: generalist
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: BBC
section: world_society
feed_url: ''
source_cap: 0
site_url: https://www.bbc.com/
source_type: public_broadcaster
authority_level: generalist
reliability_score: 5
professional_value: 4
use_role: baseline
```

```source
name: BBC World
section: world_society
feed_url: https://feeds.bbci.co.uk/news/world/rss.xml
source_cap: 6
site_url: https://www.bbc.com/news/world
source_type: public_broadcaster
authority_level: generalist
reliability_score: 5
professional_value: 4
use_role: baseline
```

```source
name: CNN
section: world_society
feed_url: http://rss.cnn.com/rss/edition.rss
source_cap: 6
site_url: https://www.cnn.com/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: NBC News
section: world_society
feed_url: https://feeds.nbcnews.com/nbcnews/public/news
source_cap: 6
site_url: https://www.nbcnews.com/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: CBS News
section: world_society
feed_url: ''
source_cap: 0
site_url: https://www.cbsnews.com/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: ABC News
section: world_society
feed_url: https://abcnews.go.com/abcnews/topstories
source_cap: 6
site_url: https://abcnews.go.com/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: DW News
section: world_society
feed_url: https://rss.dw.com/rdf/rss-en-all
source_cap: 6
site_url: https://www.dw.com/en/top-stories/s-9097
source_type: public_broadcaster
authority_level: generalist
reliability_score: 5
professional_value: 4
use_role: baseline
```

```source
name: France 24
section: world_society
feed_url: ''
source_cap: 0
site_url: https://www.france24.com/en/
source_type: public_broadcaster
authority_level: generalist
reliability_score: 5
professional_value: 4
use_role: baseline
```

```source
name: Sky News
section: world_society
feed_url: https://feeds.skynews.com/feeds/rss/world.xml
source_cap: 6
site_url: https://news.sky.com/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Al Jazeera
section: world_society
feed_url: https://www.aljazeera.com/xml/rss/all.xml
source_cap: 6
site_url: https://www.aljazeera.com/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: TRT World
section: world_society
feed_url: ''
source_cap: 0
site_url: https://www.trtworld.com/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: CGTN
section: world_society
feed_url: ''
source_cap: 0
site_url: https://www.cgtn.com/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: CBC World
section: world_society
feed_url: ''
source_cap: 0
site_url: https://www.cbc.ca/news/world
source_type: public_broadcaster
authority_level: generalist
reliability_score: 5
professional_value: 4
use_role: baseline
```

```source
name: NHK News
section: world_society
feed_url: ''
source_cap: 0
site_url: https://www3.nhk.or.jp/news/
source_type: public_broadcaster
authority_level: generalist
reliability_score: 5
professional_value: 4
use_role: baseline
```

```source
name: Euronews
section: world_society
feed_url: ''
source_cap: 0
site_url: https://www.euronews.com/news
source_type: public_broadcaster
authority_level: generalist
reliability_score: 5
professional_value: 4
use_role: baseline
```

```source
name: AllAfrica
section: world_society
feed_url: https://allafrica.com/tools/headlines/rdf/latest/headlines.rdf
source_cap: 6
site_url: https://allafrica.com/
source_type: public_broadcaster
authority_level: generalist
reliability_score: 5
professional_value: 4
use_role: baseline
```

```source
name: Africanews
section: world_society
feed_url: ''
source_cap: 0
site_url: https://www.africanews.com/
source_type: public_broadcaster
authority_level: generalist
reliability_score: 5
professional_value: 4
use_role: baseline
```

```source
name: The New York Times
section: world_society
feed_url: https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml
source_cap: 6
site_url: https://www.nytimes.com/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: The Washington Post
section: world_society
feed_url: https://feeds.washingtonpost.com/rss/world
source_cap: 6
site_url: https://www.washingtonpost.com/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: USA Today
section: world_society
feed_url: https://rssfeeds.usatoday.com/usatoday-NewsTopStories
source_cap: 6
site_url: https://www.usatoday.com/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: The Times
section: world_society
feed_url: https://www.thetimes.co.uk/rss
source_cap: 6
site_url: https://www.thetimes.co.uk/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: The Telegraph
section: world_society
feed_url: https://www.telegraph.co.uk/rss.xml
source_cap: 6
site_url: https://www.telegraph.co.uk/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: The Guardian
section: world_society
feed_url: https://www.theguardian.com/world/rss
source_cap: 6
site_url: https://www.theguardian.com/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: The Guardian World
section: world_society
feed_url: https://www.theguardian.com/world/rss
source_cap: 6
site_url: https://www.theguardian.com/world
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Frankfurter Allgemeine Zeitung / FAZ
section: world_society
feed_url: ''
source_cap: 0
site_url: https://www.faz.net/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Süddeutsche Zeitung
section: world_society
feed_url: ''
source_cap: 0
site_url: https://www.sueddeutsche.de/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Die Zeit
section: world_society
feed_url: https://newsfeed.zeit.de/index
source_cap: 6
site_url: https://www.zeit.de/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Le Monde
section: world_society
feed_url: ''
source_cap: 0
site_url: https://www.lemonde.fr/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Le Monde English – Europe
section: world_society
feed_url: https://www.lemonde.fr/en/europe/rss_full.xml
source_cap: 6
site_url: https://www.lemonde.fr/en/europe/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Le Figaro
section: world_society
feed_url: ''
source_cap: 0
site_url: https://www.lefigaro.fr/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Libération
section: world_society
feed_url: ''
source_cap: 0
site_url: https://www.liberation.fr/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Yomiuri Shimbun
section: world_society
feed_url: ''
source_cap: 0
site_url: https://www.yomiuri.co.jp/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Asahi Shimbun
section: world_society
feed_url: ''
source_cap: 0
site_url: https://www.asahi.com/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Mainichi Shimbun
section: world_society
feed_url: ''
source_cap: 0
site_url: https://mainichi.jp/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Nikkei
section: world_society
feed_url: ''
source_cap: 0
site_url: https://www.nikkei.com/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Tokyo Shimbun
section: world_society
feed_url: ''
source_cap: 0
site_url: https://www.tokyo-np.co.jp/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: The Japan Times
section: world_society
feed_url: https://www.japantimes.co.jp/feed/
source_cap: 6
site_url: https://www.japantimes.co.jp/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: South China Morning Post
section: world_society
feed_url: https://www.scmp.com/rss/91/feed
source_cap: 6
site_url: https://www.scmp.com/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: SCMP China
section: world_society
feed_url: https://www.scmp.com/rss/4/feed
source_cap: 6
site_url: https://www.scmp.com/news/china
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: 联合早报 Zaobao
section: world_society
feed_url: ''
source_cap: 0
site_url: https://www.zaobao.com.sg/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Caixin
section: world_society
feed_url: ''
source_cap: 0
site_url: https://www.caixin.com/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Caixin Weekly
section: world_society
feed_url: ''
source_cap: 0
site_url: https://weekly.caixin.com/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: The Paper 澎湃新闻
section: world_society
feed_url: https://feedx.net/rss/thepaper.xml
source_cap: 6
site_url: https://www.thepaper.cn/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: 南方周末
section: world_society
feed_url: ''
source_cap: 0
site_url: http://www.infzm.com/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: The Hindu
section: world_society
feed_url: https://www.thehindu.com/news/international/feeder/default.rss
source_cap: 6
site_url: https://www.thehindu.com/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: The Times of India
section: world_society
feed_url: ''
source_cap: 0
site_url: https://timesofindia.indiatimes.com/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: The Straits Times
section: world_society
feed_url: ''
source_cap: 0
site_url: https://www.straitstimes.com/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: The Straits Times – Asia
section: world_society
feed_url: https://www.straitstimes.com/news/asia/rss.xml
source_cap: 6
site_url: https://www.straitstimes.com/asia
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: The Jakarta Post
section: world_society
feed_url: ''
source_cap: 0
site_url: https://www.thejakartapost.com/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Channel News Asia – Asia
section: world_society
feed_url: https://www.channelnewsasia.com/api/v1/rss-outbound-feed?_format=xml&category=6511
source_cap: 6
site_url: https://www.channelnewsasia.com/asia
source_type: public_broadcaster
authority_level: generalist
reliability_score: 5
professional_value: 4
use_role: baseline
```

```source
name: Korea Herald
section: world_society
feed_url: ''
source_cap: 0
site_url: https://www.koreaherald.com/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Dawn
section: world_society
feed_url: ''
source_cap: 0
site_url: https://www.dawn.com/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Scroll.in
section: world_society
feed_url: ''
source_cap: 0
site_url: https://scroll.in/latest
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Al-Monitor
section: world_society
feed_url: ''
source_cap: 0
site_url: https://www.al-monitor.com/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Middle East Eye
section: world_society
feed_url: ''
source_cap: 0
site_url: https://www.middleeasteye.net/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: L’Orient Today
section: world_society
feed_url: ''
source_cap: 0
site_url: https://today.lorientlejour.com/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: El País América
section: world_society
feed_url: ''
source_cap: 0
site_url: https://elpais.com/america/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Latinvex
section: world_society
feed_url: ''
source_cap: 0
site_url: https://latinvex.com/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: International Crisis Group
section: world_society
feed_url: https://www.crisisgroup.org/rss.xml
source_cap: 6
site_url: https://www.crisisgroup.org/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Crisis Group – Middle East & North Africa
section: world_society
feed_url: ''
source_cap: 0
site_url: https://www.crisisgroup.org/middle-east-north-africa
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Bellingcat
section: world_society
feed_url: https://www.bellingcat.com/feed/
source_cap: 6
site_url: https://www.bellingcat.com/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: ProPublica
section: world_society
feed_url: https://feeds.propublica.org/propublica/main
source_cap: 6
site_url: https://www.propublica.org/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Council on Foreign Relations
section: world_society
feed_url: ''
source_cap: 0
site_url: https://www.cfr.org/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: European Council on Foreign Relations
section: world_society
feed_url: ''
source_cap: 0
site_url: https://ecfr.eu/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Politico
section: world_society
feed_url: https://www.politico.com/rss/politicopicks.xml
source_cap: 6
site_url: https://www.politico.com/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: POLITICO Europe
section: world_society
feed_url: https://www.politico.eu/feed/
source_cap: 6
site_url: https://www.politico.eu/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Foreign Policy
section: world_society
feed_url: https://foreignpolicy.com/feed/
source_cap: 6
site_url: https://foreignpolicy.com/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Project Syndicate
section: world_society
feed_url: https://www.project-syndicate.org/rss
source_cap: 6
site_url: https://www.project-syndicate.org/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: The Diplomat – Southeast Asia
section: world_society
feed_url: ''
source_cap: 0
site_url: https://thediplomat.com/category/regions/southeast-asia/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Americas Quarterly
section: world_society
feed_url: ''
source_cap: 0
site_url: https://www.americasquarterly.org/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: NACLA
section: world_society
feed_url: ''
source_cap: 0
site_url: https://nacla.org/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: African Arguments
section: world_society
feed_url: ''
source_cap: 0
site_url: https://africanarguments.org/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: ISS Africa
section: world_society
feed_url: ''
source_cap: 0
site_url: https://issafrica.org/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```


```source
name: NPR World
section: world_society
feed_url: https://feeds.npr.org/1004/rss.xml
source_cap: 6
site_url: https://www.npr.org/sections/world/
source_type: public_broadcaster
authority_level: generalist
reliability_score: 5
professional_value: 4
use_role: baseline
```

```source
name: PBS NewsHour World
section: world_society
feed_url: https://www.pbs.org/newshour/feeds/rss/world
source_cap: 6
site_url: https://www.pbs.org/newshour/world
source_type: public_broadcaster
authority_level: generalist
reliability_score: 5
professional_value: 4
use_role: baseline
```

```source
name: UN News
section: world_society
feed_url: https://news.un.org/feed/subscribe/en/news/all/rss.xml
source_cap: 6
site_url: https://news.un.org/en/
source_type: institutional
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: baseline
```

```source
name: Human Rights Watch
section: world_society
feed_url: https://www.hrw.org/rss/news
source_cap: 6
site_url: https://www.hrw.org/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 5
use_role: signal
```

```source
name: Amnesty International News
section: world_society
feed_url: https://www.amnesty.org/en/latest/news/feed/
source_cap: 6
site_url: https://www.amnesty.org/en/latest/news/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 5
use_role: signal
```

```source
name: UNHCR News
section: world_society
feed_url: https://www.unhcr.org/news/rss.xml
source_cap: 6
site_url: https://www.unhcr.org/news/
source_type: institutional
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: signal
```

<a id="economy"></a>

# 经济 / economy

<a id="prices_markets"></a>

## 价格与市场 / prices_markets

```section
id: prices_markets
title: prices markets
title_zh: 价格与市场
description_zh: ''
```

```source
name: World Bank Commodity Markets
section: prices_markets
feed_url: https://www.worldbank.org/en/research/commodity-markets/rss
source_cap: 6
site_url: https://www.worldbank.org/en/research/commodity-markets
source_type: institutional
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: IMF Primary Commodity Prices
section: prices_markets
feed_url: ''
source_cap: 0
site_url: https://www.imf.org/en/research/commodity-prices
source_type: institutional
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: FRED Commodities
section: prices_markets
feed_url: ''
source_cap: 0
site_url: https://fred.stlouisfed.org/categories/32217
source_type: institutional
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: Trading Economics Commodities
section: prices_markets
feed_url: ''
source_cap: 0
site_url: https://tradingeconomics.com/commodities
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Investing.com Commodities
section: prices_markets
feed_url: ''
source_cap: 0
site_url: https://www.investing.com/commodities/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Our World in Data
section: prices_markets
feed_url: https://ourworldindata.org/atom.xml
source_cap: 6
site_url: https://ourworldindata.org/
source_type: institutional
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: baseline
```


```source
name: World Bank Data Blog
section: prices_markets
feed_url: https://blogs.worldbank.org/en/opendata/feed
source_cap: 6
site_url: https://blogs.worldbank.org/en/opendata
source_type: institutional
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: reference
```

<a id="energy_resources"></a>

## 能源与资源 / energy_resources

```section
id: energy_resources
title: energy resources
title_zh: 能源与资源
description_zh: ''
```

```source
name: EIA Today in Energy
section: energy_resources
feed_url: https://www.eia.gov/rss/todayinenergy.xml
source_cap: 6
site_url: https://www.eia.gov/todayinenergy/
source_type: newspaper_magazine
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: baseline
```

```source
name: EIA What's New
section: energy_resources
feed_url: ''
source_cap: 0
site_url: https://www.eia.gov/about/new/
source_type: newspaper_magazine
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: baseline
```

```source
name: IEA News
section: energy_resources
feed_url: ''
source_cap: 0
site_url: https://www.iea.org/news
source_type: institutional
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: baseline
```

```source
name: Oilprice.com
section: energy_resources
feed_url: https://oilprice.com/rss/main
source_cap: 6
site_url: https://oilprice.com/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Reuters Energy
section: energy_resources
feed_url: ''
source_cap: 0
site_url: https://www.reuters.com/business/energy/
source_type: wire_service
authority_level: generalist
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: Carbon Brief
section: energy_resources
feed_url: ''
source_cap: 0
site_url: https://www.carbonbrief.org/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

<a id="food_agriculture_markets"></a>

## 食物与农业市场 / food_agriculture_markets

```section
id: food_agriculture_markets
title: food agriculture markets
title_zh: 食物与农业市场
description_zh: ''
```

```source
name: FAO Food Price Index
section: food_agriculture_markets
feed_url: ''
source_cap: 0
site_url: https://www.fao.org/worldfoodsituation/foodpricesindex/en/
source_type: institutional
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: FAO Food Price Monitoring
section: food_agriculture_markets
feed_url: ''
source_cap: 0
site_url: https://www.fao.org/giews/food-prices/home/en/
source_type: institutional
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: USDA ERS
section: food_agriculture_markets
feed_url: ''
source_cap: 0
site_url: https://www.ers.usda.gov/
source_type: newspaper_magazine
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: baseline
```

```source
name: USDA WASDE
section: food_agriculture_markets
feed_url: ''
source_cap: 0
site_url: https://www.usda.gov/oce/commodity/wasde
source_type: newspaper_magazine
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: baseline
```

```source
name: Food Business News
section: food_agriculture_markets
feed_url: ''
source_cap: 0
site_url: https://www.foodbusinessnews.net/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: World Grain
section: food_agriculture_markets
feed_url: ''
source_cap: 0
site_url: https://www.world-grain.com/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

<a id="housing_living_costs"></a>

## 居住与生活成本 / housing_living_costs

```section
id: housing_living_costs
title: housing living costs
title_zh: 居住与生活成本
description_zh: ''
```

```source
name: BLS CPI Average Prices
section: housing_living_costs
feed_url: ''
source_cap: 0
site_url: https://www.bls.gov/cpi/factsheets/average-prices.htm
source_type: newspaper_magazine
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: baseline
```

```source
name: FRED CPI
section: housing_living_costs
feed_url: ''
source_cap: 0
site_url: https://fred.stlouisfed.org/categories/9
source_type: institutional
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: Zillow Research
section: housing_living_costs
feed_url: ''
source_cap: 0
site_url: https://www.zillow.com/research/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Apartment List Research
section: housing_living_costs
feed_url: ''
source_cap: 0
site_url: https://www.apartmentlist.com/research
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Numbeo Cost of Living
section: housing_living_costs
feed_url: ''
source_cap: 0
site_url: https://www.numbeo.com/cost-of-living/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

<a id="supply_chains_trade"></a>

## 供应链与贸易 / supply_chains_trade

```section
id: supply_chains_trade
title: supply chains trade
title_zh: 供应链与贸易
description_zh: ''
```

```source
name: FreightWaves
section: supply_chains_trade
feed_url: https://www.freightwaves.com/news/feed
source_cap: 6
site_url: https://www.freightwaves.com/news
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: The Loadstar
section: supply_chains_trade
feed_url: https://theloadstar.com/feed/
source_cap: 6
site_url: https://theloadstar.com/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: gCaptain
section: supply_chains_trade
feed_url: ''
source_cap: 0
site_url: https://gcaptain.com/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Supply Chain Dive
section: supply_chains_trade
feed_url: ''
source_cap: 0
site_url: https://www.supplychaindive.com/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Port Technology
section: supply_chains_trade
feed_url: ''
source_cap: 0
site_url: https://www.porttechnology.org/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```


```source
name: WTO News
section: supply_chains_trade
feed_url: https://www.wto.org/english/news_e/news_e.rss
source_cap: 6
site_url: https://www.wto.org/english/news_e/news_e.htm
source_type: institutional
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: Supply Chain Management Review
section: supply_chains_trade
feed_url: https://www.scmr.com/rss/topic/all
source_cap: 6
site_url: https://www.scmr.com/
source_type: trade_publication
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Logistics Management
section: supply_chains_trade
feed_url: https://www.logisticsmgmt.com/rss/topic/all
source_cap: 6
site_url: https://www.logisticsmgmt.com/
source_type: trade_publication
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

<a id="industry_business"></a>

## 产业与商业 / industry_business

```section
id: industry_business
title: industry business
title_zh: 产业与商业
description_zh: ''
```

```source
name: Marketplace
section: industry_business
feed_url: https://www.marketplace.org/feed/
source_cap: 6
site_url: https://www.marketplace.org/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Retail Dive
section: industry_business
feed_url: ''
source_cap: 0
site_url: https://www.retaildive.com/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Modern Retail
section: industry_business
feed_url: ''
source_cap: 0
site_url: https://www.modernretail.co/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Business of Fashion
section: industry_business
feed_url: https://www.businessoffashion.com/arc/outboundfeeds/rss/?outputType=xml
source_cap: 6
site_url: https://www.businessoffashion.com/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Harvard Business Review
section: industry_business
feed_url: https://hbr.org/rss
source_cap: 6
site_url: https://hbr.org/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```


```source
name: World Bank Blogs
section: industry_business
feed_url: https://blogs.worldbank.org/en/feed
source_cap: 6
site_url: https://blogs.worldbank.org/en
source_type: institutional
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: baseline
```

<a id="money_finance"></a>

## 货币与金融 / money_finance

```section
id: money_finance
title: money finance
title_zh: 货币与金融
description_zh: ''
```

```source
name: Bank for International Settlements
section: money_finance
feed_url: https://www.bis.org/list/press_releases/index.rss
source_cap: 6
site_url: https://www.bis.org/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: IMF Blog
section: money_finance
feed_url: https://www.imf.org/en/Blogs/RSS
source_cap: 6
site_url: https://www.imf.org/en/Blogs
source_type: institutional
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: Federal Reserve Press Releases
section: money_finance
feed_url: https://www.federalreserve.gov/feeds/press_all.xml
source_cap: 6
site_url: https://www.federalreserve.gov/newsevents/pressreleases.htm
source_type: newspaper_magazine
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: baseline
```

```source
name: Financial Times
section: money_finance
feed_url: ''
source_cap: 0
site_url: https://www.ft.com/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Financial Times Markets
section: money_finance
feed_url: https://www.ft.com/markets?format=rss
source_cap: 6
site_url: https://www.ft.com/markets
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Wall Street Journal
section: money_finance
feed_url: ''
source_cap: 0
site_url: https://www.wsj.com/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Bloomberg
section: money_finance
feed_url: ''
source_cap: 0
site_url: https://www.bloomberg.com/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Reuters Markets
section: money_finance
feed_url: ''
source_cap: 0
site_url: https://www.reuters.com/markets/
source_type: wire_service
authority_level: generalist
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: CEPR VoxEU
section: money_finance
feed_url: https://cepr.org/rss/vox-content
source_cap: 6
site_url: https://cepr.org/voxeu
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: CEPR Discussion Papers
section: money_finance
feed_url: ''
source_cap: 0
site_url: https://cepr.org/research/discussion-papers
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: European Central Bank
section: money_finance
feed_url: ''
source_cap: 0
site_url: https://www.ecb.europa.eu/
source_type: institutional
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: NBER
section: money_finance
feed_url: https://www.nber.org/rss/new.xml
source_cap: 6
site_url: https://www.nber.org/
source_type: institutional
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: Nikkei Asia
section: money_finance
feed_url: ''
source_cap: 0
site_url: https://asia.nikkei.com/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Caixin Global
section: money_finance
feed_url: https://www.caixinglobal.com/rss/
source_cap: 6
site_url: https://www.caixinglobal.com/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Handelsblatt
section: money_finance
feed_url: ''
source_cap: 0
site_url: https://www.handelsblatt.com/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Les Echos
section: money_finance
feed_url: ''
source_cap: 0
site_url: https://www.lesechos.fr/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```


```source
name: OECD Newsroom
section: money_finance
feed_url: https://www.oecd.org/newsroom/publicationsdocuments/rss.xml
source_cap: 6
site_url: https://www.oecd.org/newsroom/
source_type: institutional
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: Bank of England News
section: money_finance
feed_url: https://www.bankofengland.co.uk/rss/news
source_cap: 6
site_url: https://www.bankofengland.co.uk/news
source_type: institutional
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: Brookings Economy
section: money_finance
feed_url: https://www.brookings.edu/topic/economics/feed/
source_cap: 6
site_url: https://www.brookings.edu/topic/economics/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 5
use_role: baseline
```

<a id="ideas"></a>

# 观念 / ideas

<a id="public_ideas"></a>

## 公共观念 / public_ideas

```section
id: public_ideas
title: public ideas
title_zh: 公共观念
description_zh: ''
```

```source
name: Aeon
section: public_ideas
feed_url: https://aeon.co/feed.rss
source_cap: 6
site_url: https://aeon.co/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Noema Magazine
section: public_ideas
feed_url: https://www.noemamag.com/feed/
source_cap: 6
site_url: https://www.noemamag.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: The Marginalian
section: public_ideas
feed_url: https://www.themarginalian.org/feed/
source_cap: 6
site_url: https://www.themarginalian.org/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Philosophy Now
section: public_ideas
feed_url: https://philosophynow.org/rss
source_cap: 6
site_url: https://philosophynow.org
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: 3:16 – Philosophy Magazine
section: public_ideas
feed_url: ''
source_cap: 0
site_url: https://www.316am.site
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: The Philosophical Salon
section: public_ideas
feed_url: ''
source_cap: 0
site_url: https://thephilosophicalsalon.com
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Academy of Ideas
section: public_ideas
feed_url: ''
source_cap: 0
site_url: https://academyofideas.com
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: LessWrong
section: public_ideas
feed_url: https://www.lesswrong.com/feed.xml
source_cap: 6
site_url: https://www.lesswrong.com
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Big Think
section: public_ideas
feed_url: https://bigthink.com/feed/
source_cap: 6
site_url: https://bigthink.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: The Free Press
section: public_ideas
feed_url: ''
source_cap: 0
site_url: https://www.thefp.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Comment Magazine
section: public_ideas
feed_url: ''
source_cap: 0
site_url: https://comment.org
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```


```source
name: The Conversation Philosophy
section: public_ideas
feed_url: https://theconversation.com/global/topics/philosophy-38/articles.atom
source_cap: 6
site_url: https://theconversation.com/global/topics/philosophy-38
source_type: specialist_media
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Boston Review
section: public_ideas
feed_url: https://www.bostonreview.net/feed/
source_cap: 6
site_url: https://www.bostonreview.net/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Philosopher's Magazine
section: public_ideas
feed_url: https://www.philosophersmag.com/rss
source_cap: 6
site_url: https://www.philosophersmag.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Crooked Timber
section: public_ideas
feed_url: https://crookedtimber.org/feed/
source_cap: 6
site_url: https://crookedtimber.org/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

<a id="scholarly_ideas"></a>

## 学术观念 / scholarly_ideas

```section
id: scholarly_ideas
title: scholarly ideas
title_zh: 学术观念
description_zh: ''
```

```source
name: JSTOR Daily
section: scholarly_ideas
feed_url: https://daily.jstor.org/feed/
source_cap: 6
site_url: https://daily.jstor.org/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Public Books
section: scholarly_ideas
feed_url: https://www.publicbooks.org/feed/
source_cap: 6
site_url: https://www.publicbooks.org/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: LSE Review of Books
section: scholarly_ideas
feed_url: https://blogs.lse.ac.uk/lsereviewofbooks/feed/
source_cap: 6
site_url: https://blogs.lse.ac.uk/lsereviewofbooks/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Stanford Encyclopedia of Philosophy
section: scholarly_ideas
feed_url: ''
source_cap: 0
site_url: https://plato.stanford.edu/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: reference
```

```source
name: Internet Encyclopedia of Philosophy
section: scholarly_ideas
feed_url: ''
source_cap: 0
site_url: https://iep.utm.edu/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: reference
```

```source
name: Britannica
section: scholarly_ideas
feed_url: ''
source_cap: 0
site_url: https://www.britannica.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Oxford Reference
section: scholarly_ideas
feed_url: ''
source_cap: 0
site_url: https://www.oxfordreference.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: PhilPapers
section: scholarly_ideas
feed_url: ''
source_cap: 0
site_url: https://philpapers.org/
source_type: reference_tool
authority_level: aggregator
reliability_score: 5
professional_value: 5
use_role: reference
```

```source
name: PhilArchive
section: scholarly_ideas
feed_url: ''
source_cap: 0
site_url: https://philarchive.org/
source_type: reference_tool
authority_level: primary
reliability_score: 4
professional_value: 5
use_role: reference
```

```source
name: Google Scholar
section: scholarly_ideas
feed_url: ''
source_cap: 0
site_url: https://scholar.google.com/
source_type: reference_tool
authority_level: aggregator
reliability_score: 5
professional_value: 5
use_role: reference
```

```source
name: Semantic Scholar
section: scholarly_ideas
feed_url: ''
source_cap: 0
site_url: https://www.semanticscholar.org/
source_type: reference_tool
authority_level: aggregator
reliability_score: 5
professional_value: 5
use_role: reference
```

```source
name: JSTOR
section: scholarly_ideas
feed_url: ''
source_cap: 0
site_url: https://www.jstor.org/
source_type: reference_tool
authority_level: aggregator
reliability_score: 5
professional_value: 5
use_role: reference
```

```source
name: Project MUSE
section: scholarly_ideas
feed_url: ''
source_cap: 0
site_url: https://muse.jhu.edu/
source_type: reference_tool
authority_level: aggregator
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: Notre Dame Philosophical Reviews
section: scholarly_ideas
feed_url: ''
source_cap: 0
site_url: https://ndpr.nd.edu/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: reference
```

```source
name: Mind
section: scholarly_ideas
feed_url: ''
source_cap: 0
site_url: https://academic.oup.com/mind
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: The Philosophical Review
section: scholarly_ideas
feed_url: ''
source_cap: 0
site_url: https://read.dukeupress.edu/the-philosophical-review
source_type: journal
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: Noûs
section: scholarly_ideas
feed_url: ''
source_cap: 0
site_url: https://onlinelibrary.wiley.com/journal/14680068
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Philosophical Studies
section: scholarly_ideas
feed_url: ''
source_cap: 0
site_url: https://link.springer.com/journal/11098
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Synthese
section: scholarly_ideas
feed_url: ''
source_cap: 0
site_url: https://link.springer.com/journal/11229
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Ethics
section: scholarly_ideas
feed_url: ''
source_cap: 0
site_url: https://www.journals.uchicago.edu/toc/et/current
source_type: journal
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: Philosophy & Public Affairs
section: scholarly_ideas
feed_url: ''
source_cap: 0
site_url: https://onlinelibrary.wiley.com/journal/10884963
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Journal of the History of Ideas
section: scholarly_ideas
feed_url: ''
source_cap: 0
site_url: https://jhi.pennpress.org
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: European Journal of Analytic Philosophy
section: scholarly_ideas
feed_url: ''
source_cap: 0
site_url: https://ejap.lumina.org
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Theory, Culture & Society
section: scholarly_ideas
feed_url: ''
source_cap: 0
site_url: https://journals.sagepub.com/home/tcs
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Cultural Sociology
section: scholarly_ideas
feed_url: ''
source_cap: 0
site_url: https://journals.sagepub.com/home/cus
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Journal of Classical Sociology
section: scholarly_ideas
feed_url: ''
source_cap: 0
site_url: https://journals.sagepub.com/home/csi
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Poetics
section: scholarly_ideas
feed_url: ''
source_cap: 0
site_url: https://www.sciencedirect.com/journal/poetics
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Institute of Historical Research
section: scholarly_ideas
feed_url: ''
source_cap: 0
site_url: https://www.history.ac.uk/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: American Historical Association
section: scholarly_ideas
feed_url: ''
source_cap: 0
site_url: https://www.historians.org/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Stanford Encyclopedia – Philosophy of Religion
section: scholarly_ideas
feed_url: ''
source_cap: 0
site_url: https://plato.stanford.edu/entries/philosophy-religion/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: reference
```

```source
name: Internet Encyclopedia – Philosophy of Religion
section: scholarly_ideas
feed_url: ''
source_cap: 0
site_url: https://iep.utm.edu/philrel/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: reference
```

<a id="civilizational_critique"></a>

## 文明批评 / civilizational_critique

```section
id: civilizational_critique
title: civilizational critique
title_zh: 文明批评
description_zh: ''
```

```source
name: The New Atlantis
section: civilizational_critique
feed_url: https://www.thenewatlantis.com/feed
source_cap: 6
site_url: https://www.thenewatlantis.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: The Point
section: civilizational_critique
feed_url: https://thepointmag.com/feed/
source_cap: 6
site_url: https://thepointmag.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: The Hedgehog Review
section: civilizational_critique
feed_url: https://hedgehogreview.com/web-features.xml
source_cap: 6
site_url: https://hedgehogreview.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Palladium Magazine
section: civilizational_critique
feed_url: https://www.palladiummag.com/feed/
source_cap: 6
site_url: https://www.palladiummag.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: ARENA
section: civilizational_critique
feed_url: ''
source_cap: 0
site_url: https://arena.org.au
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: The Platypus Affiliated Society
section: civilizational_critique
feed_url: ''
source_cap: 0
site_url: https://platypus1917.org
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Synthetic Zero
section: civilizational_critique
feed_url: ''
source_cap: 0
site_url: https://syntheticzero.net
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Blue Labyrinths
section: civilizational_critique
feed_url: ''
source_cap: 0
site_url: https://bluelabyrinths.substack.com
source_type: culture_magazine
authority_level: commentary
reliability_score: 3
professional_value: 4
use_role: culture_probe
```

```source
name: Matteo Pasquinelli
section: civilizational_critique
feed_url: ''
source_cap: 0
site_url: https://matteopasquinelli.com
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Rest of World
section: civilizational_critique
feed_url: https://restofworld.org/feed/latest/
source_cap: 6
site_url: https://restofworld.org/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Real Life
section: civilizational_critique
feed_url: ''
source_cap: 0
site_url: https://reallifemag.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: The Atlantic
section: civilizational_critique
feed_url: https://www.theatlantic.com/feed/all/
source_cap: 6
site_url: https://www.theatlantic.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: The Economist
section: civilizational_critique
feed_url: https://www.economist.com/rss.xml
source_cap: 6
site_url: https://www.economist.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: The New Yorker
section: civilizational_critique
feed_url: https://www.newyorker.com/feed/everything
source_cap: 6
site_url: https://www.newyorker.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Time
section: civilizational_critique
feed_url: https://time.com/feed/
source_cap: 6
site_url: https://time.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Der Spiegel
section: civilizational_critique
feed_url: ''
source_cap: 0
site_url: https://www.spiegel.de/international/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Le Point
section: civilizational_critique
feed_url: ''
source_cap: 0
site_url: https://www.lepoint.fr/
source_type: newspaper_magazine
authority_level: generalist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: The Tablet
section: civilizational_critique
feed_url: ''
source_cap: 0
site_url: https://www.thetablet.co.uk/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: First Things
section: civilizational_critique
feed_url: ''
source_cap: 0
site_url: https://www.firstthings.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```


```source
name: Law & Liberty
section: civilizational_critique
feed_url: https://lawliberty.org/feed/
source_cap: 6
site_url: https://lawliberty.org/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Dissent Magazine
section: civilizational_critique
feed_url: https://www.dissentmagazine.org/feed/
source_cap: 6
site_url: https://www.dissentmagazine.org/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Persuasion
section: civilizational_critique
feed_url: https://www.persuasion.community/feed
source_cap: 6
site_url: https://www.persuasion.community/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

<a id="cultural_forms"></a>

# 文化形式 / cultural_forms

<a id="books"></a>

## 书籍 / books

```section
id: books
title: books
title_zh: 书籍
description_zh: ''
```

```source
name: New York Review of Books
section: books
feed_url: https://www.nybooks.com/feed/
source_cap: 6
site_url: https://www.nybooks.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: London Review of Books
section: books
feed_url: https://www.lrb.co.uk/feeds/rss
source_cap: 6
site_url: https://www.lrb.co.uk/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: LARB
section: books
feed_url: https://lareviewofbooks.org/feed/
source_cap: 6
site_url: https://lareviewofbooks.org/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Bookforum
section: books
feed_url: https://www.bookforum.com/feed
source_cap: 6
site_url: https://www.bookforum.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: The Paris Review
section: books
feed_url: ''
source_cap: 0
site_url: https://www.theparisreview.org/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Literary Hub
section: books
feed_url: https://lithub.com/feed/
source_cap: 6
site_url: https://lithub.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Five Books
section: books
feed_url: ''
source_cap: 0
site_url: https://fivebooks.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Longreads
section: books
feed_url: ''
source_cap: 0
site_url: https://longreads.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: The Guardian – The Long Read
section: books
feed_url: ''
source_cap: 0
site_url: https://www.theguardian.com/theguardian/series/the-long-read
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Internet Archive
section: books
feed_url: ''
source_cap: 0
site_url: https://archive.org/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Internet Archive Blog
section: books
feed_url: https://blog.archive.org/feed/
source_cap: 6
site_url: https://blog.archive.org/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Internet Archive Books
section: books
feed_url: ''
source_cap: 0
site_url: https://blog.archive.org/category/books/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```


```source
name: TLS
section: books
feed_url: https://www.the-tls.co.uk/rss
source_cap: 6
site_url: https://www.the-tls.co.uk/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Words Without Borders
section: books
feed_url: https://wordswithoutborders.org/feed/
source_cap: 6
site_url: https://wordswithoutborders.org/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

```source
name: Open Book Publishers Blog
section: books
feed_url: https://blogs.openbookpublishers.com/feed/
source_cap: 6
site_url: https://blogs.openbookpublishers.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: reference
```

<a id="film_moving_image"></a>

## 电影与影像 / film_moving_image

```section
id: film_moving_image
title: film moving image
title_zh: 电影与影像
description_zh: ''
```

```source
name: MUBI Notebook
section: film_moving_image
feed_url: https://mubi.com/notebook/posts.rss
source_cap: 6
site_url: https://mubi.com/notebook
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

```source
name: Little White Lies
section: film_moving_image
feed_url: ''
source_cap: 0
site_url: https://lwlies.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

```source
name: BFI
section: film_moving_image
feed_url: ''
source_cap: 0
site_url: https://www.bfi.org.uk/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

```source
name: Sight and Sound
section: film_moving_image
feed_url: ''
source_cap: 0
site_url: https://www.bfi.org.uk/sight-and-sound
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

```source
name: Film Comment
section: film_moving_image
feed_url: ''
source_cap: 0
site_url: https://www.filmcomment.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

```source
name: Reverse Shot
section: film_moving_image
feed_url: ''
source_cap: 0
site_url: https://reverseshot.org/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```


```source
name: Criterion Current
section: film_moving_image
feed_url: https://www.criterion.com/current/rss
source_cap: 6
site_url: https://www.criterion.com/current
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

```source
name: RogerEbert.com
section: film_moving_image
feed_url: https://www.rogerebert.com/feed
source_cap: 6
site_url: https://www.rogerebert.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

```source
name: The Film Stage
section: film_moving_image
feed_url: https://thefilmstage.com/feed/
source_cap: 6
site_url: https://thefilmstage.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

<a id="music_sound"></a>

## 音乐与声音 / music_sound

```section
id: music_sound
title: music sound
title_zh: 音乐与声音
description_zh: ''
```

```source
name: Bandcamp Daily
section: music_sound
feed_url: https://daily.bandcamp.com/feed
source_cap: 6
site_url: https://daily.bandcamp.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

```source
name: The Quietus
section: music_sound
feed_url: https://thequietus.com/feed/
source_cap: 6
site_url: https://thequietus.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

```source
name: Aquarium Drunkard
section: music_sound
feed_url: ''
source_cap: 0
site_url: https://aquariumdrunkard.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

```source
name: Resident Advisor
section: music_sound
feed_url: ''
source_cap: 0
site_url: https://ra.co/news
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

```source
name: Pitchfork
section: music_sound
feed_url: ''
source_cap: 0
site_url: https://pitchfork.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

```source
name: Pitchfork Album Reviews
section: music_sound
feed_url: https://pitchfork.com/rss/reviews/albums/
source_cap: 6
site_url: https://pitchfork.com/reviews/albums/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```


```source
name: Stereogum
section: music_sound
feed_url: https://www.stereogum.com/feed/
source_cap: 6
site_url: https://www.stereogum.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

```source
name: The Wire Magazine
section: music_sound
feed_url: https://www.thewire.co.uk/rss
source_cap: 6
site_url: https://www.thewire.co.uk/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

```source
name: Tone Glow
section: music_sound
feed_url: https://toneglow.substack.com/feed
source_cap: 6
site_url: https://toneglow.substack.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

<a id="photography"></a>

## 摄影 / photography

```section
id: photography
title: photography
title_zh: 摄影
description_zh: ''
```

```source
name: Magnum Photos
section: photography
feed_url: ''
source_cap: 0
site_url: https://www.magnumphotos.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: baseline
```


```source
name: British Journal of Photography
section: photography
feed_url: https://www.1854.photography/feed/
source_cap: 6
site_url: https://www.1854.photography/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

```source
name: LensCulture
section: photography
feed_url: https://www.lensculture.com/articles.rss
source_cap: 6
site_url: https://www.lensculture.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

```source
name: Aperture
section: photography
feed_url: https://aperture.org/feed/
source_cap: 6
site_url: https://aperture.org/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

<a id="arts_design"></a>

## 艺术与设计 / arts_design

```section
id: arts_design
title: arts design
title_zh: 艺术与设计
description_zh: ''
```

```source
name: e-flux
section: arts_design
feed_url: https://www.e-flux.com/rss/
source_cap: 6
site_url: https://www.e-flux.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

```source
name: ArtReview
section: arts_design
feed_url: https://artreview.com/feed/
source_cap: 6
site_url: https://artreview.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

```source
name: The Art Newspaper
section: arts_design
feed_url: ''
source_cap: 0
site_url: https://www.theartnewspaper.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

```source
name: Hyperallergic
section: arts_design
feed_url: ''
source_cap: 0
site_url: https://hyperallergic.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

```source
name: ARTnews
section: arts_design
feed_url: https://www.artnews.com/feed/
source_cap: 6
site_url: https://www.artnews.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

```source
name: Cabinet Magazine
section: arts_design
feed_url: ''
source_cap: 0
site_url: https://www.cabinetmagazine.org/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

```source
name: Eye on Design
section: arts_design
feed_url: ''
source_cap: 0
site_url: https://eyeondesign.aiga.org/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

```source
name: Creative Boom
section: arts_design
feed_url: ''
source_cap: 0
site_url: https://www.creativeboom.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

```source
name: The Artist
section: arts_design
feed_url: ''
source_cap: 0
site_url: https://theartistmagazine.co.uk/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

```source
name: The Public Domain Review
section: arts_design
feed_url: https://publicdomainreview.org/rss.xml
source_cap: 6
site_url: https://publicdomainreview.org/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```


```source
name: Frieze
section: arts_design
feed_url: https://www.frieze.com/rss.xml
source_cap: 6
site_url: https://www.frieze.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

```source
name: Design Week
section: arts_design
feed_url: https://www.designweek.co.uk/feed/
source_cap: 6
site_url: https://www.designweek.co.uk/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

```source
name: Design Observer
section: arts_design
feed_url: https://designobserver.com/feed/
source_cap: 6
site_url: https://designobserver.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

<a id="architecture_urbanism"></a>

## 建筑与城市 / architecture_urbanism

```section
id: architecture_urbanism
title: architecture urbanism
title_zh: 建筑与城市
description_zh: ''
```

```source
name: Places Journal
section: architecture_urbanism
feed_url: ''
source_cap: 0
site_url: https://placesjournal.org/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

```source
name: Dezeen
section: architecture_urbanism
feed_url: https://www.dezeen.com/feed/
source_cap: 6
site_url: https://www.dezeen.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

```source
name: ArchDaily
section: architecture_urbanism
feed_url: https://www.archdaily.com/rss
source_cap: 6
site_url: https://www.archdaily.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

```source
name: The Architectural Review
section: architecture_urbanism
feed_url: ''
source_cap: 0
site_url: https://www.architectural-review.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```


```source
name: The Urbanist
section: architecture_urbanism
feed_url: https://www.theurbanist.org/feed/
source_cap: 6
site_url: https://www.theurbanist.org/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

```source
name: CityLab
section: architecture_urbanism
feed_url: https://www.bloomberg.com/feeds/citylab.rss
source_cap: 6
site_url: https://www.bloomberg.com/citylab
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Planetizen
section: architecture_urbanism
feed_url: https://www.planetizen.com/news/feed
source_cap: 6
site_url: https://www.planetizen.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

<a id="games"></a>

## 游戏与科幻 / games

```section
id: games
title: games
title_zh: 游戏与科幻
description_zh: ''
```

```source
name: Game Developer
section: games
feed_url: https://www.gamedeveloper.com/rss.xml
source_cap: 6
site_url: https://www.gamedeveloper.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

```source
name: Rock Paper Shotgun
section: games
feed_url: https://www.rockpapershotgun.com/feed
source_cap: 6
site_url: https://www.rockpapershotgun.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

```source
name: Eurogamer
section: games
feed_url: ''
source_cap: 0
site_url: https://www.eurogamer.net/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

```source
name: Polygon
section: games
feed_url: ''
source_cap: 0
site_url: https://www.polygon.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

```source
name: PC Gamer
section: games
feed_url: ''
source_cap: 0
site_url: https://www.pcgamer.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

```source
name: Tor.com
section: games
feed_url: ''
source_cap: 0
site_url: https://www.tor.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

```source
name: Superjump Magazine
section: games
feed_url: ''
source_cap: 0
site_url: https://www.superjumpmagazine.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

```source
name: Game Studies
section: games
feed_url: ''
source_cap: 0
site_url: http://gamestudies.org/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

```source
name: SFRA Review
section: games
feed_url: ''
source_cap: 0
site_url: https://sfra.org/sfra-review
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```


```source
name: Noema Games
section: games
feed_url: https://www.noemamag.com/tag/games/feed/
source_cap: 6
site_url: https://www.noemamag.com/tag/games/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

```source
name: Critical Distance
section: games
feed_url: https://critical-distance.com/feed/
source_cap: 6
site_url: https://critical-distance.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

```source
name: GamesIndustry.biz
section: games
feed_url: https://www.gamesindustry.biz/rss
source_cap: 6
site_url: https://www.gamesindustry.biz/
source_type: trade_publication
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

<a id="fashion_style"></a>

## 时尚与风格 / fashion_style

```section
id: fashion_style
title: fashion style
title_zh: 时尚与风格
description_zh: ''
```

```source
name: Business of Fashion
section: fashion_style
feed_url: https://www.businessoffashion.com/arc/outboundfeeds/rss/?outputType=xml
source_cap: 6
site_url: https://www.businessoffashion.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

```source
name: Vogue
section: fashion_style
feed_url: https://www.vogue.com/feed/rss
source_cap: 6
site_url: https://www.vogue.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

```source
name: Hypebeast
section: fashion_style
feed_url: ''
source_cap: 0
site_url: https://hypebeast.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

```source
name: Highsnobiety
section: fashion_style
feed_url: ''
source_cap: 0
site_url: https://www.highsnobiety.com/
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```


```source
name: Vogue Runway
section: fashion_style
feed_url: https://www.vogue.com/fashion-shows/rss
source_cap: 6
site_url: https://www.vogue.com/fashion-shows
source_type: culture_magazine
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: culture_probe
```

<a id="human_studies"></a>

# 人类研究 / human_studies

<a id="human_societies"></a>

## 人类社会 / human_societies

```section
id: human_societies
title: human societies
title_zh: 人类社会
description_zh: ''
```

```source
name: SAPIENS
section: human_societies
feed_url: https://www.sapiens.org/feed/
source_cap: 6
site_url: https://www.sapiens.org/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Somatosphere
section: human_societies
feed_url: http://somatosphere.net/feed/
source_cap: 6
site_url: http://somatosphere.net/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Anthropology News
section: human_societies
feed_url: https://www.anthropology-news.org/feed/
source_cap: 6
site_url: https://www.anthropology-news.org/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: The Society Pages
section: human_societies
feed_url: https://thesocietypages.org/feed/
source_cap: 6
site_url: https://thesocietypages.org/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Society for Cultural Anthropology
section: human_societies
feed_url: ''
source_cap: 0
site_url: https://culanth.org/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Allegra Lab
section: human_societies
feed_url: ''
source_cap: 0
site_url: https://allegralaboratory.net/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Annual Reviews Magazine
section: human_societies
feed_url: ''
source_cap: 0
site_url: https://www.annualreviews.org/magazine
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: The Conversation – Society
section: human_societies
feed_url: ''
source_cap: 0
site_url: https://theconversation.com/global/topics/society-63
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Contexts
section: human_societies
feed_url: ''
source_cap: 0
site_url: https://contexts.org/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```


```source
name: Anthropology Today
section: human_societies
feed_url: https://rai.onlinelibrary.wiley.com/action/showFeed?type=etoc&feed=rss&jc=14678322
source_cap: 6
site_url: https://rai.onlinelibrary.wiley.com/journal/14678322
source_type: journal
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: reference
```

```source
name: American Anthropologist
section: human_societies
feed_url: https://anthrosource.onlinelibrary.wiley.com/action/showFeed?type=etoc&feed=rss&jc=15481433
source_cap: 6
site_url: https://anthrosource.onlinelibrary.wiley.com/journal/15481433
source_type: journal
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: reference
```

```source
name: Nature Human Behaviour
section: human_societies
feed_url: https://www.nature.com/nathumbehav.rss
source_cap: 6
site_url: https://www.nature.com/nathumbehav/
source_type: journal
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: baseline
```

<a id="mind"></a>

## 心智 / mind

```section
id: mind
title: mind
title_zh: 心智
description_zh: ''
```

```source
name: Psyche
section: mind
feed_url: https://psyche.co/feed
source_cap: 6
site_url: https://psyche.co/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: BPS Research Digest
section: mind
feed_url: https://www.bps.org.uk/research-digest/rss.xml
source_cap: 6
site_url: https://www.bps.org.uk/research-digest
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: APA News
section: mind
feed_url: https://www.apa.org/news/rss
source_cap: 6
site_url: https://www.apa.org/news
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Mind & Life Institute
section: mind
feed_url: ''
source_cap: 0
site_url: https://www.mindandlife.org/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```


```source
name: BPS News
section: mind
feed_url: https://www.bps.org.uk/news-and-policy/rss.xml
source_cap: 6
site_url: https://www.bps.org.uk/news-and-policy
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Psychological Science
section: mind
feed_url: https://journals.sagepub.com/action/showFeed?type=etoc&feed=rss&jc=pssa
source_cap: 6
site_url: https://journals.sagepub.com/home/pss
source_type: journal
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: reference
```

<a id="nature"></a>

# 自然 / nature

<a id="science_news"></a>

## 科学新闻 / science_news

```section
id: science_news
title: science news
title_zh: 科学新闻
description_zh: ''
```

```source
name: ScienceDaily
section: science_news
feed_url: https://www.sciencedaily.com/rss/all.xml
source_cap: 6
site_url: https://www.sciencedaily.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Phys.org
section: science_news
feed_url: https://phys.org/rss-feed/
source_cap: 6
site_url: https://phys.org/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Phys.org Biology
section: science_news
feed_url: ''
source_cap: 0
site_url: https://phys.org/biology-news/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Science News
section: science_news
feed_url: https://www.sciencenews.org/feed
source_cap: 6
site_url: https://www.sciencenews.org/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: The Scientist
section: science_news
feed_url: https://www.the-scientist.com/rss
source_cap: 6
site_url: https://www.the-scientist.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: MIT News
section: science_news
feed_url: https://news.mit.edu/rss/topic/science-technology
source_cap: 6
site_url: https://news.mit.edu/topic/science-technology
source_type: institutional
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: baseline
```

```source
name: Quanta Magazine
section: science_news
feed_url: https://www.quantamagazine.org/feed/
source_cap: 6
site_url: https://www.quantamagazine.org/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Nautilus
section: science_news
feed_url: https://nautil.us/feed/
source_cap: 6
site_url: https://nautil.us/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Undark Magazine
section: science_news
feed_url: ''
source_cap: 0
site_url: https://undark.org/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: The Conversation Science
section: science_news
feed_url: ''
source_cap: 0
site_url: https://theconversation.com/global/topics/science-59
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: SciURLs
section: science_news
feed_url: ''
source_cap: 0
site_url: https://sciurls.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Science X
section: science_news
feed_url: ''
source_cap: 0
site_url: https://sciencex.com/news/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Neuroscience News
section: science_news
feed_url: https://neurosciencenews.com/feed/
source_cap: 6
site_url: https://neurosciencenews.com
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Live Science
section: science_news
feed_url: https://www.livescience.com/feeds/all
source_cap: 6
site_url: https://www.livescience.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

<a id="science_magazines"></a>

## 科普杂志 / science_magazines

```section
id: science_magazines
title: science magazines
title_zh: 科普杂志
description_zh: ''
```

```source
name: Scientific American
section: science_magazines
feed_url: https://rss.sciam.com/ScientificAmerican-Global
source_cap: 6
site_url: https://www.scientificamerican.com
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Discover Magazine
section: science_magazines
feed_url: https://www.discovermagazine.com/rss/all
source_cap: 6
site_url: https://www.discovermagazine.com
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Popular Science
section: science_magazines
feed_url: https://www.popsci.com/feed/
source_cap: 6
site_url: https://www.popsci.com
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: New Scientist
section: science_magazines
feed_url: ''
source_cap: 0
site_url: https://www.newscientist.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Aeon – Science
section: science_magazines
feed_url: ''
source_cap: 0
site_url: https://aeon.co/science
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

<a id="research"></a>

## 学术研究 / research

```section
id: research
title: research
title_zh: 学术研究
description_zh: ''
```

```source
name: Nature
section: research
feed_url: https://www.nature.com/nature.rss
source_cap: 6
site_url: https://www.nature.com/nature/
source_type: journal
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: Science
section: research
feed_url: https://www.science.org/action/showFeed?type=etoc&feed=rss&jc=science
source_cap: 6
site_url: https://www.science.org/journal/science
source_type: journal
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: PNAS
section: research
feed_url: https://www.pnas.org/action/showFeed?type=etoc&feed=rss&jc=pnas
source_cap: 6
site_url: https://www.pnas.org/
source_type: journal
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: The Lancet
section: research
feed_url: https://www.thelancet.com/rssfeed/lancet_current.xml
source_cap: 6
site_url: https://www.thelancet.com/
source_type: journal
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: Cell
section: research
feed_url: https://www.cell.com/cell/inpress.rss
source_cap: 6
site_url: https://www.cell.com/
source_type: journal
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: Physical Review Letters
section: research
feed_url: https://feeds.aps.org/rss/recent/prl.xml
source_cap: 6
site_url: https://journals.aps.org/prl/
source_type: journal
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: Journal of High Energy Physics
section: research
feed_url: ''
source_cap: 0
site_url: https://link.springer.com/journal/13130
source_type: journal
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: Nature Medicine
section: research
feed_url: ''
source_cap: 0
site_url: https://www.nature.com/nm/
source_type: journal
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: Nature Neuroscience
section: research
feed_url: ''
source_cap: 0
site_url: https://www.nature.com/neuro/
source_type: journal
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: Neuron
section: research
feed_url: ''
source_cap: 0
site_url: https://www.cell.com/neuron
source_type: journal
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: Science Advances
section: research
feed_url: ''
source_cap: 0
site_url: https://www.science.org/journal/sciadv
source_type: journal
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: Nature Communications
section: research
feed_url: ''
source_cap: 0
site_url: https://www.nature.com/ncomms/
source_type: journal
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: arXiv
section: research
feed_url: https://rss.arxiv.org/rss/physics
source_cap: 6
site_url: https://arxiv.org/
source_type: preprint
authority_level: primary
reliability_score: 4
professional_value: 5
use_role: signal
```

```source
name: arXiv q-bio Populations and Evolution
section: research
feed_url: ''
source_cap: 0
site_url: https://arxiv.org/list/q-bio.PE/recent
source_type: preprint
authority_level: primary
reliability_score: 4
professional_value: 5
use_role: signal
```

```source
name: bioRxiv
section: research
feed_url: https://www.biorxiv.org/rss/current.xml
source_cap: 6
site_url: https://www.biorxiv.org/
source_type: preprint
authority_level: primary
reliability_score: 4
professional_value: 5
use_role: signal
```

```source
name: bioRxiv Ecology
section: research
feed_url: https://www.biorxiv.org/rss/collection/ecology.xml
source_cap: 6
site_url: https://www.biorxiv.org/collection/ecology
source_type: preprint
authority_level: primary
reliability_score: 4
professional_value: 5
use_role: signal
```

```source
name: bioRxiv Evolutionary Biology
section: research
feed_url: ''
source_cap: 0
site_url: https://www.biorxiv.org/collection/evolutionary-biology
source_type: preprint
authority_level: primary
reliability_score: 4
professional_value: 5
use_role: signal
```

```source
name: bioRxiv Zoology
section: research
feed_url: ''
source_cap: 0
site_url: https://www.biorxiv.org/collection/zoology
source_type: preprint
authority_level: primary
reliability_score: 4
professional_value: 5
use_role: signal
```

```source
name: medRxiv
section: research
feed_url: https://www.medrxiv.org/rss/current.xml
source_cap: 6
site_url: https://www.medrxiv.org/
source_type: preprint
authority_level: primary
reliability_score: 4
professional_value: 5
use_role: signal
```

```source
name: PubMed
section: research
feed_url: ''
source_cap: 0
site_url: https://pubmed.ncbi.nlm.nih.gov/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: reference
```

```source
name: Semantic Scholar
section: research
feed_url: ''
source_cap: 0
site_url: https://www.semanticscholar.org/
source_type: reference_tool
authority_level: aggregator
reliability_score: 5
professional_value: 5
use_role: reference
```

```source
name: eLife Latest
section: research
feed_url: ''
source_cap: 0
site_url: https://elifesciences.org/
source_type: journal
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: PLOS Biology
section: research
feed_url: ''
source_cap: 0
site_url: https://journals.plos.org/plosbiology/
source_type: journal
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: PsyArXiv
section: research
feed_url: ''
source_cap: 0
site_url: https://osf.io/preprints/psyarxiv
source_type: preprint
authority_level: primary
reliability_score: 4
professional_value: 5
use_role: signal
```

```source
name: SocArXiv
section: research
feed_url: ''
source_cap: 0
site_url: https://osf.io/preprints/socarxiv
source_type: preprint
authority_level: primary
reliability_score: 4
professional_value: 5
use_role: signal
```


```source
name: Nature Ecology & Evolution
section: research
feed_url: https://www.nature.com/natecolevol.rss
source_cap: 6
site_url: https://www.nature.com/natecolevol/
source_type: journal
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: Current Biology
section: research
feed_url: https://www.cell.com/current-biology/inpress.rss
source_cap: 6
site_url: https://www.cell.com/current-biology/home
source_type: journal
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: Ecology Letters
section: research
feed_url: https://onlinelibrary.wiley.com/action/showFeed?type=etoc&feed=rss&jc=14610248
source_cap: 6
site_url: https://onlinelibrary.wiley.com/journal/14610248
source_type: journal
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: Methods in Ecology and Evolution
section: research
feed_url: https://besjournals.onlinelibrary.wiley.com/action/showFeed?type=etoc&feed=rss&jc=2041210x
source_cap: 6
site_url: https://besjournals.onlinelibrary.wiley.com/journal/2041210x
source_type: journal
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: reference
```

```source
name: PLOS ONE Biology
section: research
feed_url: https://journals.plos.org/plosone/feed/atom
source_cap: 6
site_url: https://journals.plos.org/plosone/
source_type: journal
authority_level: primary
reliability_score: 4
professional_value: 4
use_role: signal
```

<a id="space_astronomy"></a>

## 航天与宇宙 / space_astronomy

```section
id: space_astronomy
title: space astronomy
title_zh: 航天与宇宙
description_zh: ''
```

```source
name: Space.com
section: space_astronomy
feed_url: https://www.space.com/feeds/all
source_cap: 6
site_url: https://www.space.com
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Universe Today
section: space_astronomy
feed_url: https://www.universetoday.com/feed/
source_cap: 6
site_url: https://www.universetoday.com
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: NASA News
section: space_astronomy
feed_url: https://www.nasa.gov/feed/
source_cap: 6
site_url: https://www.nasa.gov/news/
source_type: institutional
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: ESA News
section: space_astronomy
feed_url: https://www.esa.int/rssfeed/Our_Activities/Space_News
source_cap: 6
site_url: https://www.esa.int/Newsroom
source_type: institutional
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: NASA Earth Observatory
section: space_astronomy
feed_url: ''
source_cap: 0
site_url: https://science.nasa.gov/earth/earth-observatory/
source_type: institutional
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: 星链
section: space_astronomy
feed_url: ''
source_cap: 0
site_url: https://satellitemap.space/index.html
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Next Rocket
section: space_astronomy
feed_url: ''
source_cap: 0
site_url: https://nextrocket.space
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```


```source
name: NASA Earth Observatory Image of the Day
section: space_astronomy
feed_url: https://earthobservatory.nasa.gov/feeds/image-of-the-day.rss
source_cap: 6
site_url: https://earthobservatory.nasa.gov/images
source_type: institutional
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: baseline
```

<a id="natural_history"></a>

## 自然史 / natural_history

```section
id: natural_history
title: natural history
title_zh: 自然史
description_zh: ''
```

```source
name: Smithsonian Science
section: natural_history
feed_url: https://www.smithsonianmag.com/rss/science-nature/
source_cap: 6
site_url: https://www.smithsonianmag.com/science-nature/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Smithsonian Smart News
section: natural_history
feed_url: ''
source_cap: 0
site_url: https://www.smithsonianmag.com/smart-news/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Natural History Museum
section: natural_history
feed_url: https://www.nhm.ac.uk/discover.rss
source_cap: 6
site_url: https://www.nhm.ac.uk/discover.html
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Everything Dinosaur
section: natural_history
feed_url: ''
source_cap: 0
site_url: https://blog.everythingdinosaur.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: DNA Writer
section: natural_history
feed_url: ''
source_cap: 0
site_url: https://earthsciweb.org/js/bio/dna-writer/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Integbio 生命科学系データベースカタログ
section: natural_history
feed_url: ''
source_cap: 0
site_url: https://integbio.jp/dbcatalog/?lang=ja
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: そらいろネット 三浦半島身近な図鑑
section: natural_history
feed_url: ''
source_cap: 0
site_url: https://sorairo-net.com/index.html
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Maryland Nature
section: natural_history
feed_url: ''
source_cap: 0
site_url: https://youtube.com/@marylandnature
source_type: video_channel
authority_level: community
reliability_score: 3
professional_value: 3
use_role: reference
```

```source
name: BBC Earth
section: natural_history
feed_url: ''
source_cap: 0
site_url: https://youtube.com/@bbcearth
source_type: public_broadcaster
authority_level: generalist
reliability_score: 5
professional_value: 4
use_role: baseline
```

<a id="ecology_conservation"></a>

## 生态与保护 / ecology_conservation

```section
id: ecology_conservation
title: ecology conservation
title_zh: 生态与保护
description_zh: ''
```

```source
name: Mongabay Conservation
section: ecology_conservation
feed_url: ''
source_cap: 0
site_url: https://news.mongabay.com/list/conservation/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Mongabay Biodiversity
section: ecology_conservation
feed_url: ''
source_cap: 0
site_url: https://news.mongabay.com/list/biodiversity/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: bioGraphic
section: ecology_conservation
feed_url: ''
source_cap: 0
site_url: https://www.biographic.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Yale Environment 360
section: ecology_conservation
feed_url: https://e360.yale.edu/rss.xml
source_cap: 6
site_url: https://e360.yale.edu/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```


```source
name: NOAA Climate.gov
section: ecology_conservation
feed_url: https://www.climate.gov/news-features/feed
source_cap: 6
site_url: https://www.climate.gov/news-features
source_type: institutional
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: baseline
```

```source
name: Inside Climate News
section: ecology_conservation
feed_url: https://insideclimatenews.org/feed/
source_cap: 6
site_url: https://insideclimatenews.org/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: The Revelator
section: ecology_conservation
feed_url: https://therevelator.org/feed/
source_cap: 6
site_url: https://therevelator.org/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

<a id="animal_behavior"></a>

## 动物行为 / animal_behavior

```section
id: animal_behavior
title: animal behavior
title_zh: 动物行为
description_zh: ''
```

```source
name: Mongabay Animal Behavior
section: animal_behavior
feed_url: ''
source_cap: 0
site_url: https://news.mongabay.com/list/animal-behavior/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Animal Cognition
section: animal_behavior
feed_url: ''
source_cap: 0
site_url: https://www.springer.com/journal/10071
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Animal Behaviour
section: animal_behavior
feed_url: https://www.sciencedirect.com/journal/animal-behaviour/rss
source_cap: 6
site_url: https://www.sciencedirect.com/journal/animal-behaviour
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```


```source
name: Behavioral Ecology
section: animal_behavior
feed_url: https://academic.oup.com/rss/site_5271/3361.xml
source_cap: 6
site_url: https://academic.oup.com/beheco
source_type: journal
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: reference
```

```source
name: Journal of Experimental Biology
section: animal_behavior
feed_url: https://journals.biologists.com/rss/site_1006/1007.xml
source_cap: 6
site_url: https://journals.biologists.com/jeb
source_type: journal
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: reference
```

<a id="marine_life"></a>

## 海洋生命 / marine_life

```section
id: marine_life
title: marine life
title_zh: 海洋生命
description_zh: ''
```

```source
name: Hakai Magazine
section: marine_life
feed_url: https://hakaimagazine.com/feed/
source_cap: 6
site_url: https://hakaimagazine.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: ScienceDaily Marine Biology
section: marine_life
feed_url: ''
source_cap: 0
site_url: https://www.sciencedaily.com/news/plants_animals/marine_biology/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: NOAA PMEL Highlights
section: marine_life
feed_url: https://www.pmel.noaa.gov/rss.xml
source_cap: 6
site_url: https://www.pmel.noaa.gov/
source_type: institutional
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: baseline
```

```source
name: NOAA Ocean Exploration
section: marine_life
feed_url: https://oceanexplorer.noaa.gov/news/oceanexplorer-news.xml
source_cap: 6
site_url: https://oceanexplorer.noaa.gov/news/
source_type: institutional
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: baseline
```

```source
name: MarineBio Conservation Society
section: marine_life
feed_url: https://www.marinebio.org/feed/
source_cap: 6
site_url: https://www.marinebio.org/news/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Oceanographic Magazine
section: marine_life
feed_url: https://oceanographicmagazine.com/feed/
source_cap: 6
site_url: https://oceanographicmagazine.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: The Revelator Oceans
section: marine_life
feed_url: https://therevelator.org/category/oceans/feed/
source_cap: 6
site_url: https://therevelator.org/category/oceans/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Mongabay Oceans
section: marine_life
feed_url: ''
source_cap: 0
site_url: https://news.mongabay.com/list/oceans/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```


```source
name: ICES Journal of Marine Science
section: marine_life
feed_url: https://academic.oup.com/rss/site_5267/3362.xml
source_cap: 6
site_url: https://academic.oup.com/icesjms
source_type: journal
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: reference
```

```source
name: Marine Ecology Progress Series
section: marine_life
feed_url: https://www.int-res.com/rss/meps.xml
source_cap: 6
site_url: https://www.int-res.com/journals/meps/
source_type: journal
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: reference
```

<a id="fish_ichthyology"></a>

## 鱼类与鱼类学 / fish_ichthyology

```section
id: fish_ichthyology
title: fish ichthyology
title_zh: 鱼类与鱼类学
description_zh: ''
```

```source
name: 我が家のHomepage 沖縄伊豆佐渡などの魚図鑑
section: fish_ichthyology
feed_url: ''
source_cap: 0
site_url: https://www.asahi-net.or.jp/~rq5y-igc/index.html
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: 沖縄の魚図鑑 ファンダイブ撮影
section: fish_ichthyology
feed_url: ''
source_cap: 0
site_url: https://okinawa-fishes.sakura.ne.jp/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: 市場魚貝類図鑑
section: fish_ichthyology
feed_url: ''
source_cap: 0
site_url: https://www.zukan-bouz.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```


```source
name: FishBase News
section: fish_ichthyology
feed_url: https://www.fishbase.se/rss/rss.xml
source_cap: 6
site_url: https://www.fishbase.se/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: reference
```

```source
name: Freshwater and Marine Image Bank
section: fish_ichthyology
feed_url: ''
source_cap: 0
site_url: https://digitalcollections.lib.washington.edu/digital/collection/fishimages
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

<a id="mollusks"></a>

## 贝壳与软体动物 / mollusks

```section
id: mollusks
title: mollusks
title_zh: 贝壳与软体动物
description_zh: ''
```

```source
name: ScienceDaily Mollusks
section: mollusks
feed_url: https://www.sciencedaily.com/rss/plants_animals/mollusks.xml
source_cap: 6
site_url: https://www.sciencedaily.com/news/plants_animals/mollusks/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Phys.org Mollusks
section: mollusks
feed_url: https://phys.org/rss-feed/search/?search=mollusks
source_cap: 6
site_url: https://phys.org/tags/mollusks/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: The Cephalopod Page
section: mollusks
feed_url: ''
source_cap: 0
site_url: https://www.thecephalopodpage.org/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Malacological Society of London
section: mollusks
feed_url: ''
source_cap: 0
site_url: https://malacsoc.org.uk/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: 貝の図鑑 主に日本の貝
section: mollusks
feed_url: ''
source_cap: 0
site_url: https://kai-zukan.info
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: 微小貝データベース
section: mollusks
feed_url: ''
source_cap: 0
site_url: https://bishogai.com/index.html
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: 微小貝さがしサポート図鑑
section: mollusks
feed_url: ''
source_cap: 0
site_url: http://bishogai-sagashi.jp
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: 雉猫の宝
section: mollusks
feed_url: ''
source_cap: 0
site_url: https://www.cypraea.jp/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: 月刊 沖縄と貝 with 光
section: mollusks
feed_url: ''
source_cap: 0
site_url: http://shellbox.blog106.fc2.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: 台灣貝類圖鑑
section: mollusks
feed_url: ''
source_cap: 0
site_url: http://shells.tw
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Conchology, Inc.
section: mollusks
feed_url: ''
source_cap: 0
site_url: https://conchology.be/?t=1
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Seahorse and Co
section: mollusks
feed_url: ''
source_cap: 0
site_url: https://www.seahorseandco.com/identificationguides
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Shell Brothers
section: mollusks
feed_url: ''
source_cap: 0
site_url: https://www.shellbrothers.be/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: SWF Beach Life
section: mollusks
feed_url: ''
source_cap: 0
site_url: https://youtube.com/@swfbeachlife
source_type: video_channel
authority_level: community
reliability_score: 3
professional_value: 3
use_role: reference
```

```source
name: Shelling Adventures
section: mollusks
feed_url: ''
source_cap: 0
site_url: https://youtube.com/@shellingadventures
source_type: video_channel
authority_level: community
reliability_score: 3
professional_value: 3
use_role: reference
```


```source
name: Journal of Molluscan Studies
section: mollusks
feed_url: https://academic.oup.com/rss/site_5275/3365.xml
source_cap: 6
site_url: https://academic.oup.com/mollus
source_type: journal
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: reference
```

<a id="arthropods"></a>

## 节肢动物 / arthropods

```section
id: arthropods
title: arthropods
title_zh: 节肢动物
description_zh: ''
```

```source
name: Entomology Today
section: arthropods
feed_url: https://entomologytoday.org/feed/
source_cap: 6
site_url: https://entomologytoday.org/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: ScienceDaily Insects
section: arthropods
feed_url: ''
source_cap: 0
site_url: https://www.sciencedaily.com/news/plants_animals/insects_and_butterflies/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Xerces Society Blog
section: arthropods
feed_url: https://xerces.org/blog/feed
source_cap: 6
site_url: https://xerces.org/blog
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: BugGuide Recent Articles
section: arthropods
feed_url: ''
source_cap: 0
site_url: https://bugguide.net/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: AntWiki Recent Changes
section: arthropods
feed_url: ''
source_cap: 0
site_url: https://www.antwiki.org/wiki/Main_Page
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Zootaxa
section: arthropods
feed_url: ''
source_cap: 0
site_url: https://mapress.com/zt/index
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: 進化する昆虫図鑑 昆虫生態写真データベース
section: arthropods
feed_url: ''
source_cap: 0
site_url: http://www.ha.shotoku.ac.jp/~kawa/KYO/SEIBUTSU/DOUBUTSU/500KonchuTop/index.html
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: 昆虫図鑑 主に日本の昆虫
section: arthropods
feed_url: ''
source_cap: 0
site_url: https://konchu-zukan.info
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: 嘎嘎昆虫网 台灣昆蟲譜
section: arthropods
feed_url: ''
source_cap: 0
site_url: http://gaga.biodiv.tw/9701bx/in94.htm
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: 昆蟲圖庫 南港國小
section: arthropods
feed_url: ''
source_cap: 0
site_url: http://icontent.nkps.tp.edu.tw/insectinfo/OrderShow.aspx?orderID=13
source_type: specialist_media
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: baseline
```

```source
name: 補鳥蛛實驗室
section: arthropods
feed_url: ''
source_cap: 0
site_url: https://thetarantulalab.com
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: くわかぶプラネット
section: arthropods
feed_url: ''
source_cap: 0
site_url: https://www.kuwakabuplanet.com
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: InsecthausTV
section: arthropods
feed_url: ''
source_cap: 0
site_url: https://youtube.com/@insecthaustv
source_type: video_channel
authority_level: community
reliability_score: 3
professional_value: 3
use_role: reference
```

```source
name: おーちゃんねる
section: arthropods
feed_url: ''
source_cap: 0
site_url: https://youtube.com/@ohchan_ch
source_type: video_channel
authority_level: community
reliability_score: 3
professional_value: 3
use_role: reference
```


```source
name: ZooKeys
section: arthropods
feed_url: https://zookeys.pensoft.net/lib/ajax_srv/article_elements_srv.php?action=rss
source_cap: 6
site_url: https://zookeys.pensoft.net/
source_type: journal
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: reference
```

```source
name: Insect Systematics and Diversity
section: arthropods
feed_url: https://academic.oup.com/rss/site_5248/3394.xml
source_cap: 6
site_url: https://academic.oup.com/isd
source_type: journal
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: reference
```

```source
name: Journal of Insect Science
section: arthropods
feed_url: https://academic.oup.com/rss/site_5248/3368.xml
source_cap: 6
site_url: https://academic.oup.com/jinsectscience
source_type: journal
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: reference
```

```source
name: PeerJ Arthropod Biology
section: arthropods
feed_url: https://peerj.com/articles/index.xml?subject=arthropod-biology
source_cap: 6
site_url: https://peerj.com/subjects/arthropod-biology/
source_type: journal
authority_level: primary
reliability_score: 4
professional_value: 4
use_role: signal
```

<a id="plants_fungi"></a>

## 植物与真菌 / plants_fungi

```section
id: plants_fungi
title: plants fungi
title_zh: 植物与真菌
description_zh: ''
```

```source
name: Kew Science
section: plants_fungi
feed_url: ''
source_cap: 0
site_url: https://www.kew.org/science
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: New Phytologist
section: plants_fungi
feed_url: https://nph.onlinelibrary.wiley.com/action/showFeed?type=etoc&feed=rss&jc=14698137
source_cap: 6
site_url: https://nph.onlinelibrary.wiley.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: 植物智
section: plants_fungi
feed_url: ''
source_cap: 0
site_url: https://www.iplant.cn/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```


```source
name: Botany One
section: plants_fungi
feed_url: https://botany.one/feed/
source_cap: 6
site_url: https://botany.one/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: American Journal of Botany
section: plants_fungi
feed_url: https://bsapubs.onlinelibrary.wiley.com/action/showFeed?type=etoc&feed=rss&jc=15372197
source_cap: 6
site_url: https://bsapubs.onlinelibrary.wiley.com/journal/15372197
source_type: journal
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: reference
```

```source
name: MycoKeys
section: plants_fungi
feed_url: https://mycokeys.pensoft.net/lib/ajax_srv/article_elements_srv.php?action=rss
source_cap: 6
site_url: https://mycokeys.pensoft.net/
source_type: journal
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: reference
```

<a id="minerals_geology"></a>

## 矿物与地质 / minerals_geology

```section
id: minerals_geology
title: minerals geology
title_zh: 矿物与地质
description_zh: ''
```

```source
name: 鉱物たちの庭
section: minerals_geology
feed_url: ''
source_cap: 0
site_url: https://lapisps.sakura.ne.jp/index.html
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```


```source
name: Mindat News
section: minerals_geology
feed_url: https://www.mindat.org/rss.php
source_cap: 6
site_url: https://www.mindat.org/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: reference
```

```source
name: USGS News
section: minerals_geology
feed_url: https://www.usgs.gov/news/rss.xml
source_cap: 6
site_url: https://www.usgs.gov/news
source_type: institutional
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: baseline
```

```source
name: Geology Page
section: minerals_geology
feed_url: https://www.geologypage.com/feed
source_cap: 6
site_url: https://www.geologypage.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 3
professional_value: 3
use_role: signal
```

<a id="technology"></a>

# 技术 / technology

<a id="ai_systems"></a>

## AI 系统 / ai_systems

```section
id: ai_systems
title: ai systems
title_zh: AI 系统
description_zh: ''
```

```source
name: MIT Technology Review
section: ai_systems
feed_url: ''
source_cap: 0
site_url: https://www.technologyreview.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Google AI Blog
section: ai_systems
feed_url: ''
source_cap: 0
site_url: https://blog.google/technology/ai/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Google DeepMind
section: ai_systems
feed_url: https://deepmind.google/blog/rss.xml
source_cap: 6
site_url: https://deepmind.google/blog/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: The Verge AI
section: ai_systems
feed_url: ''
source_cap: 0
site_url: https://www.theverge.com/ai-artificial-intelligence
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: The Gradient
section: ai_systems
feed_url: ''
source_cap: 0
site_url: https://thegradient.pub/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Hugging Face Blog
section: ai_systems
feed_url: https://huggingface.co/blog/feed.xml
source_cap: 6
site_url: https://huggingface.co/blog
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Stanford HAI
section: ai_systems
feed_url: https://hai.stanford.edu/news/rss.xml
source_cap: 6
site_url: https://hai.stanford.edu/
source_type: institutional
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: baseline
```

```source
name: Stanford AI Index
section: ai_systems
feed_url: ''
source_cap: 0
site_url: https://hai.stanford.edu/ai-index
source_type: institutional
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: baseline
```


```source
name: OpenAI News
section: ai_systems
feed_url: https://openai.com/news/rss.xml
source_cap: 6
site_url: https://openai.com/news/
source_type: institutional
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: Anthropic News
section: ai_systems
feed_url: https://www.anthropic.com/news/rss.xml
source_cap: 6
site_url: https://www.anthropic.com/news
source_type: institutional
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: Meta AI Blog
section: ai_systems
feed_url: https://ai.meta.com/blog/rss/
source_cap: 6
site_url: https://ai.meta.com/blog/
source_type: institutional
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: Microsoft Research Blog
section: ai_systems
feed_url: https://www.microsoft.com/en-us/research/feed/
source_cap: 6
site_url: https://www.microsoft.com/en-us/research/blog/
source_type: institutional
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: Distill
section: ai_systems
feed_url: https://distill.pub/rss.xml
source_cap: 6
site_url: https://distill.pub/
source_type: specialist_media
authority_level: specialist
reliability_score: 5
professional_value: 5
use_role: reference
```

<a id="computing_cultures"></a>

## 计算文化 / computing_cultures

```section
id: computing_cultures
title: computing cultures
title_zh: 计算文化
description_zh: ''
```

```source
name: Ars Technica
section: computing_cultures
feed_url: https://feeds.arstechnica.com/arstechnica/index
source_cap: 6
site_url: https://arstechnica.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Simon Willison's Weblog
section: computing_cultures
feed_url: https://simonwillison.net/atom/everything/
source_cap: 6
site_url: https://simonwillison.net/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: LWN.net
section: computing_cultures
feed_url: https://lwn.net/headlines/rss
source_cap: 6
site_url: https://lwn.net/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Communications of the ACM
section: computing_cultures
feed_url: https://cacm.acm.org/feed/
source_cap: 6
site_url: https://cacm.acm.org/feed/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Hacker News
section: computing_cultures
feed_url: https://news.ycombinator.com/rss
source_cap: 6
site_url: https://news.ycombinator.com/
source_type: reference_tool
authority_level: community
reliability_score: 3
professional_value: 4
use_role: signal
```

```source
name: hckr news
section: computing_cultures
feed_url: ''
source_cap: 0
site_url: https://hckrnews.com
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

```source
name: hackertab
section: computing_cultures
feed_url: ''
source_cap: 0
site_url: https://now.hackertab.dev
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

```source
name: HelloGitHub
section: computing_cultures
feed_url: ''
source_cap: 0
site_url: https://hellogithub.com
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Product Hunt
section: computing_cultures
feed_url: ''
source_cap: 0
site_url: https://www.producthunt.com
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: signal
```

```source
name: Techmeme
section: computing_cultures
feed_url: https://www.techmeme.com/feed.xml
source_cap: 6
site_url: https://www.techmeme.com/
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

```source
name: SoylentNews
section: computing_cultures
feed_url: https://soylentnews.org/index.rss
source_cap: 6
site_url: https://soylentnews.org
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Sentiers
section: computing_cultures
feed_url: https://sentiers.media/feed/
source_cap: 6
site_url: https://sentiers.media
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: 数学 & 物理 & 杂项
section: computing_cultures
feed_url: ''
source_cap: 0
site_url: https://t.me/math_and_physics_and_misc
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```


```source
name: ACM Queue
section: computing_cultures
feed_url: https://queue.acm.org/rss/feeds/queuecontent.xml
source_cap: 6
site_url: https://queue.acm.org/
source_type: specialist_media
authority_level: specialist
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: IEEE Computer Society
section: computing_cultures
feed_url: https://www.computer.org/csdl/rss
source_cap: 6
site_url: https://www.computer.org/
source_type: specialist_media
authority_level: specialist
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: Martin Fowler
section: computing_cultures
feed_url: https://martinfowler.com/feed.atom
source_cap: 6
site_url: https://martinfowler.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: Julia Evans
section: computing_cultures
feed_url: https://jvns.ca/atom.xml
source_cap: 6
site_url: https://jvns.ca/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

<a id="platforms_infrastructure"></a>

## 平台与基础设施 / platforms_infrastructure

```section
id: platforms_infrastructure
title: platforms infrastructure
title_zh: 平台与基础设施
description_zh: ''
```

```source
name: Cloudflare Blog
section: platforms_infrastructure
feed_url: https://blog.cloudflare.com/rss/
source_cap: 6
site_url: https://blog.cloudflare.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: GitHub Blog
section: platforms_infrastructure
feed_url: https://github.blog/feed/
source_cap: 6
site_url: https://github.blog/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: GitHub Changelog
section: platforms_infrastructure
feed_url: ''
source_cap: 0
site_url: https://github.blog/changelog/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Mozilla Hacks
section: platforms_infrastructure
feed_url: https://hacks.mozilla.org/feed/
source_cap: 6
site_url: https://hacks.mozilla.org/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Vercel Blog
section: platforms_infrastructure
feed_url: https://vercel.com/atom
source_cap: 6
site_url: https://vercel.com/blog
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: APNIC Blog
section: platforms_infrastructure
feed_url: https://blog.apnic.net/feed/
source_cap: 6
site_url: https://blog.apnic.net/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```


```source
name: Kubernetes Blog
section: platforms_infrastructure
feed_url: https://kubernetes.io/feed.xml
source_cap: 6
site_url: https://kubernetes.io/blog/
source_type: institutional
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: AWS News Blog
section: platforms_infrastructure
feed_url: https://aws.amazon.com/blogs/aws/feed/
source_cap: 6
site_url: https://aws.amazon.com/blogs/aws/
source_type: institutional
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: Google Cloud Blog
section: platforms_infrastructure
feed_url: https://cloudblog.withgoogle.com/rss/
source_cap: 6
site_url: https://cloud.google.com/blog/
source_type: institutional
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: Azure Blog
section: platforms_infrastructure
feed_url: https://azure.microsoft.com/en-us/blog/feed/
source_cap: 6
site_url: https://azure.microsoft.com/en-us/blog/
source_type: institutional
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: Netflix TechBlog
section: platforms_infrastructure
feed_url: https://netflixtechblog.com/feed
source_cap: 6
site_url: https://netflixtechblog.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 5
professional_value: 5
use_role: baseline
```

<a id="interfaces_media_technology"></a>

## 界面与媒介技术 / interfaces_media_technology

```section
id: interfaces_media_technology
title: interfaces media technology
title_zh: 界面与媒介技术
description_zh: ''
```

```source
name: The Verge
section: interfaces_media_technology
feed_url: https://www.theverge.com/rss/index.xml
source_cap: 6
site_url: https://www.theverge.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Wired
section: interfaces_media_technology
feed_url: https://www.wired.com/feed/rss
source_cap: 6
site_url: https://www.wired.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Wired – Science
section: interfaces_media_technology
feed_url: ''
source_cap: 0
site_url: https://www.wired.com/category/science/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Nielsen Norman Group
section: interfaces_media_technology
feed_url: ''
source_cap: 0
site_url: https://www.nngroup.com/articles/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Platformer
section: interfaces_media_technology
feed_url: https://www.platformer.news/feed
source_cap: 6
site_url: https://www.platformer.news/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Garbage Day
section: interfaces_media_technology
feed_url: https://www.garbageday.email/feed
source_cap: 6
site_url: https://www.garbageday.email/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Search Engine Land
section: interfaces_media_technology
feed_url: https://searchengineland.com/feed
source_cap: 6
site_url: https://searchengineland.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

<a id="cybernetics_automation"></a>

## 控制论与自动化 / cybernetics_automation

```section
id: cybernetics_automation
title: cybernetics automation
title_zh: 控制论与自动化
description_zh: ''
```

```source
name: IEEE Spectrum Robotics
section: cybernetics_automation
feed_url: https://spectrum.ieee.org/feeds/topic/robotics.rss
source_cap: 6
site_url: https://spectrum.ieee.org/robotics
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```


```source
name: IEEE Spectrum Aerospace
section: cybernetics_automation
feed_url: https://spectrum.ieee.org/feeds/topic/aerospace.rss
source_cap: 6
site_url: https://spectrum.ieee.org/aerospace
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Robotics Business Review
section: cybernetics_automation
feed_url: https://www.roboticsbusinessreview.com/feed/
source_cap: 6
site_url: https://www.roboticsbusinessreview.com/
source_type: trade_publication
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

<a id="hardware_radio_embedded"></a>

## 硬件、无线电与嵌入式 / hardware_radio_embedded

```section
id: hardware_radio_embedded
title: hardware radio embedded
title_zh: 硬件、无线电与嵌入式
description_zh: ''
```

```source
name: ARRL News
section: hardware_radio_embedded
feed_url: https://www.arrl.org/arrl.rss
source_cap: 6
site_url: https://www.arrl.org/news
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: RTL-SDR Blog
section: hardware_radio_embedded
feed_url: https://www.rtl-sdr.com/feed/
source_cap: 6
site_url: https://www.rtl-sdr.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: SWLing Post
section: hardware_radio_embedded
feed_url: https://swling.com/blog/feed/
source_cap: 6
site_url: https://swling.com/blog/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Radio Society of Great Britain
section: hardware_radio_embedded
feed_url: https://rsgb.org/main/feed/
source_cap: 6
site_url: https://rsgb.org/main/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Hackaday
section: hardware_radio_embedded
feed_url: https://hackaday.com/blog/feed/
source_cap: 6
site_url: https://hackaday.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: IEEE Spectrum
section: hardware_radio_embedded
feed_url: https://spectrum.ieee.org/feeds/feed.rss
source_cap: 6
site_url: https://spectrum.ieee.org/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: CNX Software
section: hardware_radio_embedded
feed_url: https://www.cnx-software.com/feed/
source_cap: 6
site_url: https://www.cnx-software.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Raspberry Pi Blog
section: hardware_radio_embedded
feed_url: https://www.raspberrypi.com/news/feed/
source_cap: 6
site_url: https://www.raspberrypi.com/news/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Adafruit Blog
section: hardware_radio_embedded
feed_url: https://blog.adafruit.com/feed/
source_cap: 6
site_url: https://blog.adafruit.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: SparkFun News
section: hardware_radio_embedded
feed_url: https://www.sparkfun.com/news/rss
source_cap: 6
site_url: https://www.sparkfun.com/news
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: iFixit News
section: hardware_radio_embedded
feed_url: https://www.ifixit.com/News/feed
source_cap: 6
site_url: https://www.ifixit.com/News
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```


```source
name: NVIDIA Technical Blog
section: hardware_radio_embedded
feed_url: https://developer.nvidia.com/blog/feed/
source_cap: 6
site_url: https://developer.nvidia.com/blog/
source_type: specialist_media
authority_level: specialist
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: ServeTheHome
section: hardware_radio_embedded
feed_url: https://www.servethehome.com/feed/
source_cap: 6
site_url: https://www.servethehome.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: EE Times
section: hardware_radio_embedded
feed_url: https://www.eetimes.com/feed/
source_cap: 6
site_url: https://www.eetimes.com/
source_type: trade_publication
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

<a id="ham_radio"></a>

## 业余无线电 / ham_radio

```section
id: ham_radio
title: ham radio
title_zh: 业余无线电
description_zh: ''
```

```source
name: QRZ
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://www.qrz.com
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: RadioID
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://radioid.net
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: LoTW / Logbook of The World
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://lotw.arrl.org/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: Cloudlog
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://www.magicbug.co.uk/cloudlog/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: BrandMeister
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://brandmeister.network/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: TGIF
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://tgif.network/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: D-STAR
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://www.dstar.org/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: YSF / Wires-X
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://systemfusion.yaesu.com/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: EchoLink
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://www.echolink.org/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: IRLP
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://www.irlp.net/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: AllStarLink
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://www.allstarlink.org/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: HamVoIP
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://hamvoip.org/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: DVSwitch
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://dvswitch.groups.io/g/main/wiki
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: MMDVM
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://github.com/g4klx/MMDVM
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: FT8 / WSJT-X
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://wsjt.sourceforge.io/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: WSPR
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://www.wsprnet.org/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: PSK31
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://www.psk31.com/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: APRS
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://aprs.fi/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: AX.25 Packet Radio
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://www.tapr.org/ax25.html
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: Winlink
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://winlink.org/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: Maidenhead Locator System
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://ham.c5r.app/maidenhead-grid
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: DroidStar
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://github.com/nostar/DroidStar
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: DroidStar Vocoder Servers — pizzanbeer
section: ham_radio
feed_url: ''
source_cap: 0
site_url: http://pizzanbeer.net/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: DroidStar Vocoder Servers — dudestar
section: ham_radio
feed_url: ''
source_cap: 0
site_url: http://dudestar.gw8szl.co.uk/Droidstar/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: Pi-Star
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://www.pistar.uk/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: Pi-Star Forum
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://forum.pistar.uk/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: Fldigi
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://www.w1hkj.com/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: CHIRP
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://chirpmyradio.com/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: HAM 小工具
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://ham.c5r.app
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: MIIT 中国工业和信息化部
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://www.miit.gov.cn/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: CRAC 中国无线电协会
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://www.crac.org.cn/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: 中国题库 A 新
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://exam.ham.upall.cn/?t=a_2025
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: 中国题库 B 新
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://exam.ham.upall.cn/?t=b_2025
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: 中国题库 B 模
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://ham-exam.iots.vip
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: 中国题库 C 新
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://exam.ham.upall.cn/?t=c_2025
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: FCC Amateur Radio Service
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://www.fcc.gov/wireless/bureau-divisions/mobility-division/amateur-radio-service
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: ARRL Licensing & Exams
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://www.arrl.org/licensing-education-training
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: US 题库 T
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://exam.ham.upall.cn/?t=t
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: US 题库 G
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://exam.ham.upall.cn/?t=g
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: US 题库 E
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://exam.ham.upall.cn/?t=e
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: JARL
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://www.jarl.org/English/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: MIC Japan
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://www.soumu.go.jp/english/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: Ofcom Amateur Radio
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://www.ofcom.org.uk/spectrum/radio-equipment/amateur-radio
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: RSGB Training
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://rsgb.org/main/clubs-training/training/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: Bundesnetzagentur
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://www.bundesnetzagentur.de/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: DARC
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://www.darc.de/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: CEPT
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://www.cept.org/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: CEPT Amateur Radio
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://www.cept.org/ecc/topics/amateur-radio
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: Celestrak
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://celestrak.org/NORAD/elements/supplemental/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: AMSAT Satellite Status
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://www.amsat.org/status/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: GoSatWatch
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://gosoftworks.com/apps/gosatwatch/users-guide/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: ISS Detector
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://issdetector.com/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: AMSAT
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://www.amsat.org/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: AMSAT-DL
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://amsat-dl.org/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: SatNOGS
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://satnogs.org/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: ARRL
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://www.arrl.org/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: RSGB
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://rsgb.org/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: DMR-MARC
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://www.dmr-marc.net/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: FreeDV
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://freedv.org/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: OARC
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://www.oarc.uk/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: HRCC
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://hamradiocrashcourse.com/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: eHam
section: ham_radio
feed_url: ''
source_cap: 0
site_url: https://www.eham.net/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

<a id="technology_politics"></a>

## 技术政治 / technology_politics

```section
id: technology_politics
title: technology politics
title_zh: 技术政治
description_zh: ''
```

```source
name: Electronic Frontier Foundation
section: technology_politics
feed_url: https://www.eff.org/rss/updates.xml
source_cap: 6
site_url: https://www.eff.org/updates
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Tech Policy Press
section: technology_politics
feed_url: https://www.techpolicy.press/rss/
source_cap: 6
site_url: https://www.techpolicy.press/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Rest of World
section: technology_politics
feed_url: https://restofworld.org/feed/latest/
source_cap: 6
site_url: https://restofworld.org/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: 404 Media
section: technology_politics
feed_url: https://www.404media.co/rss/
source_cap: 6
site_url: https://www.404media.co/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: The Markup
section: technology_politics
feed_url: https://themarkup.org/feeds/rss.xml
source_cap: 6
site_url: https://themarkup.org/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```

```source
name: Access Now
section: technology_politics
feed_url: https://www.accessnow.org/feed/
source_cap: 6
site_url: https://www.accessnow.org/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: baseline
```


```source
name: Schneier on Security
section: technology_politics
feed_url: https://www.schneier.com/feed/atom/
source_cap: 6
site_url: https://www.schneier.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: Krebs on Security
section: technology_politics
feed_url: https://krebsonsecurity.com/feed/
source_cap: 6
site_url: https://krebsonsecurity.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 5
professional_value: 5
use_role: baseline
```

```source
name: Lawfare Cyber
section: technology_politics
feed_url: https://www.lawfaremedia.org/topic/cybersecurity/feed
source_cap: 6
site_url: https://www.lawfaremedia.org/topic/cybersecurity
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 5
use_role: baseline
```

<a id="material"></a>

# 器物 / material

<a id="field_gear"></a>

## 野外装备 / field_gear

```section
id: field_gear
title: field gear
title_zh: 野外装备
description_zh: ''
```

```source
name: OutdoorGearLab
section: field_gear
feed_url: https://www.outdoorgearlab.com/feed
source_cap: 6
site_url: https://www.outdoorgearlab.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 3
professional_value: 4
use_role: culture_probe
```

```source
name: SectionHiker
section: field_gear
feed_url: https://sectionhiker.com/feed/
source_cap: 6
site_url: https://sectionhiker.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 3
professional_value: 4
use_role: culture_probe
```

```source
name: Field Mag
section: field_gear
feed_url: https://www.fieldmag.com/rss
source_cap: 6
site_url: https://www.fieldmag.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 3
professional_value: 4
use_role: culture_probe
```

```source
name: Bikepacking.com
section: field_gear
feed_url: https://bikepacking.com/feed/
source_cap: 6
site_url: https://bikepacking.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 3
professional_value: 4
use_role: culture_probe
```

```source
name: Gear Patrol
section: field_gear
feed_url: https://www.gearpatrol.com/rss/
source_cap: 6
site_url: https://www.gearpatrol.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 3
professional_value: 4
use_role: culture_probe
```

```source
name: KnifeNews
section: field_gear
feed_url: https://knifenews.com/feed/
source_cap: 6
site_url: https://knifenews.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 3
professional_value: 4
use_role: culture_probe
```

```source
name: BLADE Magazine Knife News
section: field_gear
feed_url: ''
source_cap: 0
site_url: https://blademag.com/knife-news
source_type: specialist_media
authority_level: specialist
reliability_score: 3
professional_value: 4
use_role: culture_probe
```


```source
name: Wirecutter Outdoors
section: field_gear
feed_url: https://www.nytimes.com/wirecutter/outdoors/rss/
source_cap: 6
site_url: https://www.nytimes.com/wirecutter/outdoors/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: reference
```

```source
name: Adventure Journal
section: field_gear
feed_url: https://www.adventure-journal.com/feed/
source_cap: 6
site_url: https://www.adventure-journal.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 3
use_role: culture_probe
```

```source
name: Backpacking Light
section: field_gear
feed_url: https://backpackinglight.com/feed/
source_cap: 6
site_url: https://backpackinglight.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: reference
```

<a id="everyday_carry"></a>

## 日用携行 / everyday_carry

```section
id: everyday_carry
title: everyday carry
title_zh: 日用携行
description_zh: ''
```

```source
name: Carryology
section: everyday_carry
feed_url: https://www.carryology.com/feed/
source_cap: 6
site_url: https://www.carryology.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 3
professional_value: 4
use_role: culture_probe
```

```source
name: Everyday Carry
section: everyday_carry
feed_url: https://everydaycarry.com/rss
source_cap: 6
site_url: https://everydaycarry.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 3
professional_value: 4
use_role: culture_probe
```

```source
name: Best Damn EDC
section: everyday_carry
feed_url: ''
source_cap: 0
site_url: https://www.bestdamnedc.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 3
professional_value: 4
use_role: culture_probe
```


```source
name: The Prepared
section: everyday_carry
feed_url: https://theprepared.com/feed/
source_cap: 6
site_url: https://theprepared.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: reference
```

```source
name: Tools and Toys
section: everyday_carry
feed_url: https://toolsandtoys.net/feed/
source_cap: 6
site_url: https://toolsandtoys.net/
source_type: specialist_media
authority_level: commentary
reliability_score: 3
professional_value: 3
use_role: culture_probe
```

<a id="tools_workshop"></a>

## 工具与工坊 / tools_workshop

```section
id: tools_workshop
title: tools workshop
title_zh: 工具与工坊
description_zh: ''
```

```source
name: 'Make:'
section: tools_workshop
feed_url: https://makezine.com/feed/
source_cap: 6
site_url: https://makezine.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 3
professional_value: 4
use_role: culture_probe
```

```source
name: Core77
section: tools_workshop
feed_url: https://www.core77.com/rss
source_cap: 6
site_url: https://www.core77.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 3
professional_value: 4
use_role: culture_probe
```

```source
name: Cool Tools
section: tools_workshop
feed_url: https://kk.org/cooltools/feed/
source_cap: 6
site_url: https://kk.org/cooltools/
source_type: specialist_media
authority_level: specialist
reliability_score: 3
professional_value: 4
use_role: culture_probe
```

```source
name: Low-Tech Magazine
section: tools_workshop
feed_url: https://solar.lowtechmagazine.com/feeds/all-en.atom.xml
source_cap: 6
site_url: https://solar.lowtechmagazine.com/
source_type: specialist_media
authority_level: specialist
reliability_score: 3
professional_value: 4
use_role: culture_probe
```

```source
name: 越後の大工道具
section: tools_workshop
feed_url: ''
source_cap: 0
site_url: https://daikuhamono.sakura.ne.jp
source_type: specialist_media
authority_level: specialist
reliability_score: 3
professional_value: 4
use_role: culture_probe
```

```source
name: 大工さんが作ったページ
section: tools_workshop
feed_url: ''
source_cap: 0
site_url: https://tyouken.tendon.bz/index.html
source_type: specialist_media
authority_level: specialist
reliability_score: 3
professional_value: 4
use_role: culture_probe
```

```source
name: Combination Wrench
section: tools_workshop
feed_url: ''
source_cap: 0
site_url: https://ameblo.jp/corgibell/
source_type: specialist_media
authority_level: specialist
reliability_score: 3
professional_value: 4
use_role: culture_probe
```


```source
name: Fine Woodworking
section: tools_workshop
feed_url: https://www.finewoodworking.com/feed
source_cap: 6
site_url: https://www.finewoodworking.com/
source_type: trade_publication
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: reference
```

```source
name: Popular Woodworking
section: tools_workshop
feed_url: https://www.popularwoodworking.com/feed/
source_cap: 6
site_url: https://www.popularwoodworking.com/
source_type: trade_publication
authority_level: specialist
reliability_score: 4
professional_value: 4
use_role: reference
```

<a id="repair_maintenance"></a>

## 维修与维护 / repair_maintenance

```section
id: repair_maintenance
title: repair maintenance
title_zh: 维修与维护
description_zh: ''
```

```source
name: iFixit News
section: repair_maintenance
feed_url: https://www.ifixit.com/News/feed
source_cap: 6
site_url: https://www.ifixit.com/News
source_type: specialist_media
authority_level: specialist
reliability_score: 3
professional_value: 4
use_role: culture_probe
```

```source
name: Repair.org
section: repair_maintenance
feed_url: https://www.repair.org/blog?format=rss
source_cap: 6
site_url: https://www.repair.org/
source_type: specialist_media
authority_level: specialist
reliability_score: 3
professional_value: 4
use_role: culture_probe
```

```source
name: The Restart Project
section: repair_maintenance
feed_url: https://therestartproject.org/feed/
source_cap: 6
site_url: https://therestartproject.org/
source_type: specialist_media
authority_level: specialist
reliability_score: 3
professional_value: 4
use_role: culture_probe
```

<a id="manuals"></a>

## 手册 / manuals

```section
id: manuals
title: manuals
title_zh: 手册
description_zh: ''
```

```source
name: SONY PCM-A10 Help Guide
section: manuals
feed_url: ''
source_cap: 0
site_url: https://helpguide.sony.net/icd/pcma10/v1/zh-cn/index.html
source_type: manual
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: Suunto Vertical User Guide (ZH)
section: manuals
feed_url: ''
source_cap: 0
site_url: https://ns.suunto.com/Manuals/Suunto_Vertical/Userguides//Suunto_Vertical_UserGuide_ZH.pdf
source_type: manual
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

<a id="reference"></a>

# 参考 / reference

<a id="reference_pool"></a>

## 参考来源暂存 / reference_pool

```section
id: reference_pool
title: reference pool
title_zh: 参考来源暂存
description_zh: ''
```

```source
name: Open Culture
section: reference_pool
feed_url: ''
source_cap: 0
site_url: http://www.openculture.com/
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

```source
name: Library Stack
section: reference_pool
feed_url: ''
source_cap: 0
site_url: https://www.librarystack.org/
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

```source
name: The Collector
section: reference_pool
feed_url: ''
source_cap: 0
site_url: https://www.thecollector.com/
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

```source
name: Programming Historian
section: reference_pool
feed_url: ''
source_cap: 0
site_url: https://programminghistorian.org/
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

```source
name: DH Now / Digital Humanities Now
section: reference_pool
feed_url: ''
source_cap: 0
site_url: https://digitalhumanitiesnow.org/
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

```source
name: Clearview Driving
section: reference_pool
feed_url: ''
source_cap: 0
site_url: https://youtube.com/@clearviewdriving
source_type: video_channel
authority_level: community
reliability_score: 3
professional_value: 3
use_role: reference
```

<a id="maps_geo_data"></a>

## 地图与地理数据 / maps_geo_data

```section
id: maps_geo_data
title: maps geo data
title_zh: 地图与地理数据
description_zh: ''
```

```source
name: Plane Crash Info
section: maps_geo_data
feed_url: ''
source_cap: 0
site_url: http://planecrashinfo.com
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

```source
name: 天地图 中国国家地理信息公共服务平台
section: maps_geo_data
feed_url: ''
source_cap: 0
site_url: https://www.tianditu.gov.cn
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: Earth Wind Map
section: maps_geo_data
feed_url: ''
source_cap: 0
site_url: https://earth.nullschool.net/#current/wind/surface/level/orthographic=-240.00,0.00,402
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

```source
name: Native Land Digital
section: maps_geo_data
feed_url: ''
source_cap: 0
site_url: https://native-land.ca
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

```source
name: City Roads
section: maps_geo_data
feed_url: ''
source_cap: 0
site_url: https://anvaka.github.io/city-roads/
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

```source
name: 全球光污染地图
section: maps_geo_data
feed_url: ''
source_cap: 0
site_url: https://www.darkmap.cn
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

```source
name: David Rumsey Map
section: maps_geo_data
feed_url: ''
source_cap: 0
site_url: https://www.davidrumsey.com/
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

```source
name: 埔里百年歷史地圖
section: maps_geo_data
feed_url: ''
source_cap: 0
site_url: https://gissrv4.sinica.edu.tw/gis/puli.html
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 4
use_role: reference
```

```source
name: 中国历史地图集
section: maps_geo_data
feed_url: ''
source_cap: 0
site_url: http://www.ccamc.co/chinese_historical_map/index.php
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

```source
name: Manhole
section: maps_geo_data
feed_url: ''
source_cap: 0
site_url: https://manhole.co.il
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

```source
name: A View From My Seat
section: maps_geo_data
feed_url: ''
source_cap: 0
site_url: https://aviewfrommyseat.com/
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

```source
name: ArcGIS Story Maps
section: maps_geo_data
feed_url: ''
source_cap: 0
site_url: https://storymaps.arcgis.com/stories/e927741a6a1c4157a1e3a91a2645f3f8
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

```source
name: 中国观景指数
section: maps_geo_data
feed_url: ''
source_cap: 0
site_url: https://viewpre.com
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

<a id="document_search"></a>

## 文档检索 / document_search

```section
id: document_search
title: document search
title_zh: 文档检索
description_zh: ''
```

```source
name: sooPAT 专利搜索
section: document_search
feed_url: ''
source_cap: 0
site_url: https://www.soopat.com
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

```source
name: All About RSS
section: document_search
feed_url: ''
source_cap: 0
site_url: https://github.com/AboutRSS/ALL-about-RSS
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```


```source
name: IEEE Xplore
section: document_search
feed_url: ''
source_cap: 0
site_url: https://ieeexplore.ieee.org/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: reference
```

```source
name: OpenAlex
section: document_search
feed_url: ''
source_cap: 0
site_url: https://openalex.org/
source_type: reference_tool
authority_level: aggregator
reliability_score: 5
professional_value: 5
use_role: reference
```

```source
name: Crossref
section: document_search
feed_url: ''
source_cap: 0
site_url: https://www.crossref.org/
source_type: reference_tool
authority_level: primary
reliability_score: 5
professional_value: 5
use_role: reference
```

<a id="rss_feed_management"></a>

## RSS 与信息管理 / rss_feed_management

```section
id: rss_feed_management
title: rss feed management
title_zh: RSS 与信息管理
description_zh: ''
```

```source
name: Feedly
section: rss_feed_management
feed_url: ''
source_cap: 0
site_url: https://feedly.com/
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

```source
name: Inoreader
section: rss_feed_management
feed_url: ''
source_cap: 0
site_url: https://www.inoreader.com/
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

```source
name: Miniflux
section: rss_feed_management
feed_url: ''
source_cap: 0
site_url: https://miniflux.app/
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

<a id="archives_aggregators"></a>

## 档案与聚合 / archives_aggregators

```section
id: archives_aggregators
title: archives aggregators
title_zh: 档案与聚合
description_zh: ''
```

```source
name: Substack Reads
section: archives_aggregators
feed_url: ''
source_cap: 0
site_url: https://on.substack.com/p/reads
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

```source
name: Medium Staff Picks
section: archives_aggregators
feed_url: ''
source_cap: 0
site_url: https://medium.com/tag/staff-picks
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

```source
name: kottke.org
section: archives_aggregators
feed_url: ''
source_cap: 0
site_url: https://kottke.org/
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```

```source
name: Philosophy Paperboy
section: archives_aggregators
feed_url: ''
source_cap: 0
site_url: http://www.philosophypaperboy.com
source_type: reference_tool
authority_level: aggregator
reliability_score: 3
professional_value: 4
use_role: reference
```


```source
name: Data is Plural
section: archives_aggregators
feed_url: https://www.data-is-plural.com/feed.xml
source_cap: 6
site_url: https://www.data-is-plural.com/
source_type: aggregator
authority_level: specialist
reliability_score: 4
professional_value: 5
use_role: signal
```

```source
name: The Browser
section: archives_aggregators
feed_url: https://thebrowser.com/feed
source_cap: 6
site_url: https://thebrowser.com/
source_type: aggregator
authority_level: commentary
reliability_score: 4
professional_value: 4
use_role: reference
```

<a id="communities_discussion"></a>

## 社区与讨论 / communities_discussion

```section
id: communities_discussion
title: communities discussion
title_zh: 社区与讨论
description_zh: ''
```

```source
name: r/worldnews
section: communities_discussion
feed_url: ''
source_cap: 0
site_url: https://www.reddit.com/r/worldnews
source_type: reference_tool
authority_level: community
reliability_score: 2
professional_value: 3
use_role: signal
```

```source
name: r/AskSocialScience
section: communities_discussion
feed_url: ''
source_cap: 0
site_url: https://www.reddit.com/r/AskSocialScience
source_type: reference_tool
authority_level: community
reliability_score: 3
professional_value: 4
use_role: reference
```

```source
name: r/Foodforthought
section: communities_discussion
feed_url: ''
source_cap: 0
site_url: https://www.reddit.com/r/Foodforthought
source_type: reference_tool
authority_level: community
reliability_score: 2
professional_value: 3
use_role: signal
```

```source
name: Philosophy Stack Exchange
section: communities_discussion
feed_url: ''
source_cap: 0
site_url: https://philosophy.stackexchange.com/
source_type: reference_tool
authority_level: community
reliability_score: 3
professional_value: 4
use_role: reference
```

---

## Notes

- citation files intentionally excluded.
- Sources without a reliable RSS feed keep `feed_url:` blank.
- Metadata is intentionally pragmatic and can be revised manually.
