from actions.actions import perform_or_specify, avatar
from models import Context


if __name__ == '__main__':

    context = None

    while True:
        text = avatar.listen()
        if context:
            context.add(text)
        else:
            context = Context(text)

        context = perform_or_specify(context)

