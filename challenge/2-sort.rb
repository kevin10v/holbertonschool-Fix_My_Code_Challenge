#!/usr/bin/env ruby
###
#
#  Sort integer arguments (ascending)
#
###

result = []
ARGV.each do |arg|
    # skip if not an integer
    next if arg !~ /^-?[0-9]+$/
    # convert to integer
    result << arg.to_i
end

result.sort!
result.each do |num|
    puts num
end
