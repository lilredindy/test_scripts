puts (0...8).map { (65 + rand(26)).chr }.join


puts (0...50).map { ('a'..'z').to_a[rand(26)] }.join


o = [('a'..'z'), ('A'..'Z')].map { |i| i.to_a }.flatten
string = (0...50).map { o[rand(o.length)] }.join
puts string


puts rand(36**5).to_s(36)


