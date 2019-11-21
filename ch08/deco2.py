class Deco:
    def __call__(self, *args, **kwargs):
        print(args)
        
dc = Deco()
dc('굼뱅이','지렁이','개구리')


