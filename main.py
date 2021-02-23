# %%
# % reset - sf
import time


def list_search(r=100000, verbose=True):
    t0 = time.time()
    n = range(3, r + 1, 2)
    p = [2]
    # print "Adding to list of primes:", 2

    while len(n) > 0:
        # print "Now testing", n[0]

        if n[0] ** 2 > r:
            if verbose:
                print "Done searching for primes"
                # print "Attach remaining vals to list of primes:", n
            p.extend(n)
            n = []
            break

        p.append(n[0])
        if verbose:
            print "Adding to list of primes:", n[0]
            # print "Checking for factors of", n[0]
        for f in range(n[0] ** 2, r + 1, 2 * n[0]):
            # print "Checking for existence of", f
            if f in n:
                # print "Factor exists, remove", f
                n.remove(f)

        n.remove(n[0])
    tf = time.time()
    dt = tf - t0
    return p, dt, r


def set_search(r=100000, verbose=True):
    t0 = time.time()
    n = set(range(3, r + 1, 2))
    p = {2}
    # print "Adding to list of primes:", 2
    print n
    while len(n) > 0:
        pnow = n.pop()
        if verbose:
            print "Now testing", pnow
        p.add(pnow)
        if pnow ** 2 > r:
            if verbose:
                print "Done searching for primes"
                # print "Attach remaining vals to list of primes:", n
            p.update(n)
            n.clear()
            break

        # print "Adding to list of primes:", pnow
        # print "Checking for factors of", pnow
        f = set(range(pnow ** 2, r + 1, 2 * pnow))
        n.difference_update(f)

    tf = time.time()
    dt = tf - t0
    return p, dt, r

def report(p, dt, r):
    print p
    print "It took", dt, "seconds to find all", len(p), "prime numbers less than", r + 1


if __name__ == "__main__":
    max_value = 100001
    talk_to_me = True
    p_list, dt_list, r_list = list_search(r=max_value, verbose=talk_to_me)
    p_set, dt_set, r_set = set_search(r=max_value, verbose=talk_to_me)
    if talk_to_me:
        report(p=p_list, dt=dt_list, r=r_list)
        report(p=p_set, dt=dt_set, r=r_set)

