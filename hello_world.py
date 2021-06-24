#import packages
import argparse

#construct the argument parse and parse the arguments
ap = argparse.ArgumentParser() #initiate the object as ap
ap.add_argument("-n", "--name", required=True , help = "name of the user")
args = vars(ap.parse_args())

#print statement
print ("Hi there {}, it's nice to meet you!".format(args["name"]))
