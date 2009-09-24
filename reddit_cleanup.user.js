// ==UserScript==
// @name           Reddit cleanup
// @namespace      com.neurobashing
// @description    Fix things I don't like about reddit
// @include        http://www.reddit.com/*
// ==/UserScript==

var creatething = document.evaluate('//div[@class="sidebox create"]', document, null, XPathResult.UNORDERED_NODE_SNAPSHOT_TYPE, null);
creatething.snapshotItem(0).style.display = 'none'
