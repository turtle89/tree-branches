import turtle


def drawBranch(branchLength):
    if branchLength > 5:
        turtle.forward(branchLength)
        turtle.right(20)
        drawBranch(branchLength - 15)
        turtle.left(40)
        drawBranch(branchLength - 15)
        turtle.right(20)
        turtle.backward(branchLength)


def main():
    turtle.left(90)
    turtle.penup()
    turtle.backward(150)
    turtle.pendown()
    drawBranch(100)
    turtle.exitonclick()


if __name__ == '__main__':
    main()
