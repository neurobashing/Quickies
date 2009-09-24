// ==UserScript==
// @name           Fuck Trends
// @namespace      com.neurobashing
// @description    I hate the stupid trends thingee
// @include        http://twitter.com/
// ==/UserScript==

var f = document.getElementById('trends');
f.style.display = 'none';

// also I hate the promotional thingee.
var promothing = document.evaluate('//p[@class="promotion round"]', document, null, XPathResult.UNORDERED_NODE_SNAPSHOT_TYPE, null);
promothing.snapshotItem(0).style.display = 'none'