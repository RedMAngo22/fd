try:
    print(eval(' '.join(prompt[1:])))
except Exception as e:
    print('eval: fail: {0}: {1}'.format(type(e).__name__, e))
