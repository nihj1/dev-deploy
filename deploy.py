# -*-coding: utf-8 -*-


if __name__ == '__main__':
    from parse import Config

    c = Config()

    conf = Config.load(c.config)

    print(conf.source.addr.priority_h)
