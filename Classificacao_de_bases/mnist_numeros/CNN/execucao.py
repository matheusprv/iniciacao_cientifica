def print_image(image):
    plt.figure()
    plt.imshow(image[0])
    plt.show
    plt.pause(0.001)

print("Realizando importações necessárias")
import load_dataset as ld
import numpy as np
import matplotlib.pyplot as plt
print("\tImportações finalizadas")



print("\nCarregando dataset de teste")
x_test, y_test = ld.load_dataset("../mnist_test.csv", 28, 28)
print("\tCarregamento de dataset concluido")



print("\nCarregando modelo")
model = ld.load_model("model.json", "model.h5")
print("\tCarregamento de modelo concluído\n")



model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# wrong = 0
# wrong_indexes = []
# for index in range (0, 10000):
#     image = x_test[index].reshape((1,28,28))
#     prediction = model.predict(image)

#     prediction = np.argmax(prediction)

#     if prediction != int(y_test[index]):
#         wrong += 1
#         wrong_indexes.append(index)
#         print("Index: ", index, " Prediction: ", prediction, " Expected: ", int(y_test[index]))

# print("\nWrong: ", wrong, "\nWrong indexes: ", wrong_indexes)

while True:
    index = input("Digite o index desejado: ")

    if index == "sair":
        break

    try:
        index = int(index)
    except:
        print("Valor inválido! Para sair, digite\"sair\"\n")
        continue

    if index > 10000 or index < 1:
        print("O valor deve estar entre 1 e 1000.\n")
        continue

    index -= 1
    image = x_test[index].reshape((1,28,28))
    print_image(image)
    prediction = model.predict(image)

    print("\nResultado encontrado: ",np.argmax(prediction))
    print("Resultado esperado: ", int(y_test[index]), "\n")