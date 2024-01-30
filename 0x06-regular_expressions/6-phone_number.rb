#!/usr/bin/env ruby
#A Ruby script that accepts one argument and pass it to a regular expression matching method
#The regular expression match a 10 digit phone number

puts ARGV[0].scan(/^[0-9]{10}$/).join
