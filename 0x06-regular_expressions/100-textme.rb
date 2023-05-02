#!/usr/bin/env ruby
puts ARGV[0].scan(/(?<=from:).+?(?=\])/).join + "," + ARGV[0].scan(/(?<=to:).+?(?=\])/).join + "," + ARGV[0].scan(/(?<=flags:).+?(?=\])/).join
