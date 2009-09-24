// ==UserScript==
// @name           Farkitall
// @namespace      com.neurobashing
// @description    get rid of fark things I never look at
// @include        http://www.fark.com/
// ==/UserScript==

var bodyRightSideContainer = document.getElementById('bodyRightSideContainer');
bodyRightSideContainer.style.display = 'none';
var bodyHeadlineContainer = document.getElementById('bodyHeadlineContainer');
bodyHeadlineContainer.style.width = '100%';
var bodyColorTabs = document.getElementById('bodyColorTabs');
bodyColorTabs.style.display = 'none';
var topMenu = document.getElementById('topMenu');
topMenu.style.display = 'none';

