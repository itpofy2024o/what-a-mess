using Pkg
Pkg.add("ArgParse")
Pkg.activate(".")
using ArgParse

function parse_commandline()
  args = ArgParseSettings()
  @add_arg_table args begin
    "--upperLimit"
      help = "the upper limit of the summation"
      arg_type= Int
      default = 0
  end
  return parse_args(args)
end

function main()
  @show parsed_args = parse_commandline()

  upperLimit = parsed_args["upperLimit"]

  ol(s) = sum(1/(factorial(big(n))) for n in 0:s)

  println(ol(upperLimit))
end

main()
