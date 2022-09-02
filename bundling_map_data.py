with open("onefile.html", "w") as output:
    with open("index.html", "r") as input_file:
        for line in input_file:
            if "DistrictsFinal.js" in line:
                print(line)

                js = open("DistrictsFinal.js").read()
                output.write(js)

            elif "Texas AFT locals.js" in line:
                print(line)

                js = open("Texas AFT locals.js").read()
                output.write(js)

            else:
                output.write(line)
