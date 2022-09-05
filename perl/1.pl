#/usr/bin perl -w
use strict;

my $sum = 0;

for (my $i=1 ; $i<1000 ; $i++) {
    if ($i%3 == 0 or $i%5 == 0) {
        $sum += $i;
    }
}

print "Sum = $sum\n";
