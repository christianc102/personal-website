---
layout: default
title: log
permalink: /log/
---

<p class="voice">random curiosities</p>

<ul class="post-list">
{% for post in site.posts %}
  <li>
    <a href="{{ post.url }}">{{ post.title }}</a>
    <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%Y.%m.%d" }}</time>
  </li>
{% endfor %}
</ul>
