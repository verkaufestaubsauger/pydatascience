# staubsauger
# creadits to Siraj
from sklearn import tree

clf = tree.DecisionTreeClassifier()
# dataset height, weight, shoesize
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]
# values connected to the dataset
Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

# trains the tree on x -> y
clf = clf.fit(X, Y)
# user input
try:
    height_input = int(input("groeße eingeben "))
    weight_input = int(input("Gewicht eingeben "))
    shoesize_input = int(input("Schuhgröße eingeben "))
except ValueError:
    exit("Nur Zahlen möglich")

prediction = clf.predict([[height_input, weight_input, shoesize_input]])
# guess of sklearn
print(prediction)
