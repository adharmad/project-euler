#/usr/bin perl -w
use strict;

my $fst = 1;
my $snd = 2;

my $sum = 2;

while ((my $next = ($fst+$snd)) < 4000000) {
    print "next = $next\n";
    if ($next%2 == 0) {
        $sum += $next;
    }

    ($fst, $snd) = ($snd, $next);
}

print "Sum = $sum";

