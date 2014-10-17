#include <iostream>
#include <string>
#include <vector>
using namespace std;

const int _a[] = { 1, 2, 3, 4, 5 };
vector <int> a( _a, _a + (sizeof( _a ) / sizeof( _a[ 0 ] )) );

int main( int argc, char* argv[] )
{
    vector <string> args( argv, argv +argc );
    
    cout << "The array a[] = ";
    for (unsigned n = 0; n < a.size(); n++)
        cout << a[ n ] << ' ';
    cout << endl;
    
    cout << "The command line arguments:\n";
    for (unsigned n = 0; n < args.size(); n++)
        cout << n << ": " << args[ n ] << endl;
    
    return 0;
}