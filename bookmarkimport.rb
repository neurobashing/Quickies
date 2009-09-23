#!/usr/bin/ruby
# -*- tab-width: 2 -*-

require 'rubygems'
require 'xml'
require 'appscript'
include Appscript

yj = app('Yojimbo')

bmfile = XML::Document.file('Webnotes.xbel')

bookmarklist = bmfile.find('//bookmark')

bookmarklist.each do |bookmark|
  yjbm = yj.make(:new => :bookmark_item)
  bookmarklink = bookmark.attributes['href']
  bookmarktitle = ''
  bookmarkdesc = ''
  bookmark.each_child do |child|
    if child.name == "title"
      bookmarktitle = child.content
    end
    if child.name == "desc"
      bookmarkdesc = child.content
    end
  end
  yjbm.location.set(bookmarklink)
  yjbm.name.set(bookmarktitle)
  yjbm.comments.set(bookmarkdesc)
end
