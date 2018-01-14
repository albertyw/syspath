from syspath import append_parent_path


append_parent_path(index=4)

if __name__ == "__main__":
    import sys
    print(sys.path[-1])
