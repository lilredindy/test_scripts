module Codebreaker
	class Game
		def initialize(output)
			@output = output
		end

		def start(secret = nil)
			@secret = secret
			@output.puts("Welcome to Codebreaker!")
			@output.puts("Enter guess:")
		end

		def guess(guess)
			marker = Codebreaker::Marker.new(@secret, guess)
			@output.puts '+'*marker.exact_match_count + '-'*marker.number_match_count
		end
	end

	class Marker
		def initialize(secret = nil, guess)
			@secret, @guess = secret, guess
		end

		#def number_match_count()
		#	(0..3).inject(0) do |count, index|
		#	count + (number_match?(index) ? 1 : 0)
		#	end
		#end

		def number_match_count
			total_match_count - exact_match_count
		end

		def total_match_count
			count = 0
			secret = @secret.split('')
			@guess.split('').map do |n|
				if secret.include?(n)
					secret.delete_at(secret.index(n))
					count +=1
				end
			end
			count
		end

		def exact_match_count()
			(0..3).inject(0) do |count, index|
			count + (exact_match?(index) ? 1 : 0)
			end
		end

		def exact_match?(index)
			@guess[index] == @secret[index]
		end

		def number_match?(index)
			@secret.include?(@guess[index]) && !exact_match?(index)
		end
	end
end


if __FILE__ == $0
#	game = Codebreaker::Game.new(STDOUT)
#	game.start('1233')
#	while guess = gets.chomp
#		game.guess(guess)
#	end

	def generate_secret_code
		options = %w[1 2 3 4 5 6]
		(1..4).map { options.delete_at(rand(options.length))}.join
	end
	
	game = Codebreaker::Game.new(STDOUT)
	secret_code = generate_secret_code
	at_exit { puts "\n***\nThe secret code was: #{secret_code}\n***"}
	game.start(secret_code)
	while guess = gets.chomp
		game.guess(guess)
	end

end
