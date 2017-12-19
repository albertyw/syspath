from syspath import append_current_path


append_current_path(index=4)

if __name__ == "__main__":
    import sys
    print(sys.path[-1])
