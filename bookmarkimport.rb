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
  yjbm.location.set(bookmark.attributes['href'])
  bookmark.each_child do |child|
    if child.name == "title"
        yjbm.name.set(child.content)
    end
    if child.name == "desc"
      yjbm.comments.set(child.content)
    end
  end
end
