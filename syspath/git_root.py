from syspath import append_git_root


append_git_root(index=5)

if __name__ == "__main__":
    import sys
    print(sys.path[-1])
