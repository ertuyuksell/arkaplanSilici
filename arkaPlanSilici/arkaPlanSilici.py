import rembg

inputPath="moutime.jpeg"#Kullanmak istediğiniz resmi urlsi ile girin

outputPath="output.png"#istediğiniz ismi verip .png(jpeg yerine png daha iyidir) yazın.

with open(inputPath, "rb") as file:
    with open(outputPath, "wb") as output:
        inputFile=file.read()
        outputFile= rembg.remove(inputFile)
        output.write(outputFile)
