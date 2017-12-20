from syspath import append_git_root


append_git_root()

if __name__ == "__main__":
    import sys
    print(sys.path[-1])
