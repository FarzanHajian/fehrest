from . import helper
import fehrest.publisher as pub
import fehrest.initializer as init


def main():
    args = helper.parse_args()
    if args.initialize:
        i = init.Initializer(site_name=args.name, path=args.output)
        i.initialize()
    elif args.publish:
        p = pub.Publisher(args.publish)
        p.publish()


if __name__ == '__main__':
    main()
