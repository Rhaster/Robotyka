
#include <iostream>
#include <fstream>
#include <queue>
#include <math.h>
#include <list>
#include <utility>
#include <array>
#include <time.h>


using namespace std;
// zmiana priority que by sortowalo po 2 elemencie malejaco 
struct myComp {
public:
    constexpr bool operator()(
        pair<array<int, 4>, double> const& a,
        pair<array<int, 4>, double> const& b)
        const noexcept
    {
        return a.second > b.second;
    }
};
bool CelZnaleziony(int x, int y, int celx, int cely)
{
    if (x == celx && y == cely)
    {
        return true;
    }
    return false;
}
using namespace std;
void wypisztab(double** tab)
{
    for (int i = 1; i < 6 + 1; i++)
    {
        for (int j = 1; j < 6 + 1; j++)
        {
            cout << " " << tab[i][j];
        }cout << "\n";
    }
}
void wypiszliste(list<pair<array<int, 4>, double>>mylist)
{
    for (const auto& it : mylist)
    {
        if (mylist.empty() == false)
        {
            cout << " " << it.first[0] << " , " << it.first[1] << " kosz baz  = " << it.first[2] << "kierunek rodzica =" << it.first[3] << " herystyka = " << it.second << endl;
        }
    }
    cout << '\n';
}

// wyliczam wartosc eurystyki dla otwartych node 
double WartoscEurystyki(double PozX, double  PozY, double CelX, double CelY, double Koszt)
{
    return Koszt + sqrt(pow(PozX - CelX, 2) + (pow(PozY - CelY, 2)));
}
//sprawdzam czy nie wykraczam poza mape 
bool czywwymiarze(int i, int j, int wym, int wym2)
{
    if ((i > 0 && i <= wym) && (j > 0 && j <= wym2))
    {
        return true;
    }
    else {
        return false;
    }
}

// sprawdza czy dany node istnieje w liscie 
int contains(list<pair<array<int, 4>, double>>& listOfElements, pair<array<int, 4>, double> element)
{
    if (listOfElements.empty() == true)
    {
        return false;
    }
    else {
        for (const auto& it : listOfElements)
        {
            if ((it.first[0] == element.first[0]) && (it.first[1] == element.first[1])) // porównanie po współrzednych 
            {
                if (it.first[2] > element.first[2])
                {
                    return 1;  // zawiera i istnieje lepsza droga wiec trzeba podmienic
                }
                else {
                    return 2; // zawiera ale jest juz korzystniejsza droga
                }
            }
        }
        return 0;
    }
}

list<pair<array<int, 4>, double>>poruszanie(double** G, int i, int j, int wym1, int wym2, int CelX, int CelY, int x, int y, int KosztBazowy, list<pair<array<int, 4>, double>>& Lista, double** tab)
{
    //do zachowania wezłów 
    //
    // KONWENCJA RUCHU
    // 0 - północ
    // 1 - południe
    // 2 - wschód 
    // 3 - zachód 
    list<pair<array<int, 4>, double>>HolderQ;
    // w góre 
    if (czywwymiarze(i - 1, j, wym1, wym2) == 1)
    {
        double holder = WartoscEurystyki(i - 1, j, CelX, CelY, KosztBazowy + 1);
        if (G[i - 1][j] != 5)
        {
            if ((contains(Lista, { {i - 1,j,KosztBazowy + 1,1},holder })) == 0 && G[i - 1][j] != 2) // ZMIANA  S!!!!!zmiana
            {
                HolderQ.push_back({ {i - 1,j,KosztBazowy + 1,1},holder });
                G[i - 1][j] = 2;
                tab[i - 1][j] = 1;
                //cout << i - 1 << " " << j << " " << holder << " Koszt bazowy " << KosztBazowy << endl;
                //wypisztab(G);
                if (CelZnaleziony(i - 1, j, CelX, CelY))
                {
                    return HolderQ;
                }
            }
        }
    }
    //w dół
    if (czywwymiarze(i + 1, j, wym1, wym2) == 1)
    {
        double holder = WartoscEurystyki(i + 1, j, CelX, CelY, KosztBazowy + 1);
        if (G[i + 1][j] != 5)
        {
            if ((contains(Lista, { {i + 1,j,KosztBazowy + 1,0},holder }) == 0) && G[i + 1][j] != 2)
            {
                HolderQ.push_back({ {i + 1,j,KosztBazowy + 1,0}, holder });
                tab[i + 1][j] = 4;
                G[i + 1][j] = 2;
                //cout << i + 1 << " " << j << " " << holder << " Koszt bazowy " << KosztBazowy << endl;
                //wypisztab(G);
                if (CelZnaleziony(i + 1, j, CelX, CelY))
                {
                    return HolderQ;
                }
            }

        }
    }
    //w lewo
    if (czywwymiarze(i, j - 1, wym1, wym2) == 1)
    {
        float holder = WartoscEurystyki(i, j - 1, CelX, CelY, KosztBazowy + 1);
        if (G[i][j - 1] != 5)
        {
            if ((contains(Lista, { {i,j - 1,KosztBazowy + 1,2},holder }) == 0) && G[i][j - 1] != 2)
            {
                tab[i][j - 1] = 2;
                HolderQ.push_back({ {i,j - 1,KosztBazowy + 1,2}, holder });
                G[i][j - 1] = 2;
                // cout << i << " " << j - 1 << " " << holder << " Koszt bazowy " << KosztBazowy + 1 << endl;
                //wypisztab(G);
                if (CelZnaleziony(i, j - 1, CelX, CelY))
                {
                    return HolderQ;
                }
            }

        }
    }
    //w prawo
    if (czywwymiarze(i, j + 1, wym1, wym2) == 1)
    {
        float holder = WartoscEurystyki(i, j + 1, CelX, CelY, KosztBazowy + 1);   // KosztBazowy + 1 albo  (abs(x - i) + abs(y - (j + 1))
        if (G[i][j + 1] != 5)
        {
            //cout << G[i][j + 1] << endl;
            if ((contains(Lista, { {i,j + 1,KosztBazowy + 1,3},holder }) == 0) && G[i][j + 1] != 2)
            {
                tab[i][j + 1] = 3;
                HolderQ.push_back({ {i,j + 1,KosztBazowy + 1,3}, holder });
                G[i][j + 1] = 2;
                //cout << i << " " << j + 1 << " " << holder << " Koszt bazowy " << KosztBazowy + 1 <<  endl;
                //wypisztab(G);
                if (CelZnaleziony(i, j + 1, CelX, CelY))
                {
                    return HolderQ;
                }
            }
        }
    }
    return HolderQ;
}
double** znajdzdroge(double** tab, double** tab2, int wym1, int wym2, int CelX, int CelY, int x, int y)
{
    // KONWENCJA RUCHU
    // 0 - północ
    // 1 - południe
    // 2 - wschód 
    // 3 - zachód 
    //cout << " WSPÓŁRZEDNE " << x << " " << y << endl;
    tab[x][y] = 3;
    while (1)
    {
        if (tab2[x][y] == 1) // góra 
        {

            // cout << " WSPÓŁRZEDNE " << x << " " << y << endl;
            tab[x][y] = 3;
            x += 1;
            //cout << " WSPÓŁRZEDNE PO 1 " << x << " " << y << endl;
        }
        else if (tab2[x][y] == 2) // prawo
        {
            //cout << " WSPÓŁRZEDNE " << x << " " << y << endl;
            tab[x][y] = 3;
            y += 1;
            //cout << " WSPÓŁRZEDNE po 2 " << x << " " << y << endl;

        }
        else if (tab2[x][y] == 3) // lewo
        {
            //cout << " WSPÓŁRZEDNE " << x << " " << y << endl;
            tab[x][y] = 3;
            y -= 1;
            //cout << " WSPÓŁRZEDNE  po 3 " << x << " " << y << endl;
        }
        else if (tab2[x][y] == 4) // dol 
        {
            //cout << " WSPÓŁRZEDNE " << x << " " << y << endl;
            tab[x][y] = 3;
            x -= 1;
            //cout << " WSPÓŁRZEDNE  4 " << x << " " << y << endl;
        }
        else if (tab2[x][y] == 5) {
            //cout << "znaleziono" << endl;
            tab[x][y] = 3;
            break;
        }
        else {
            //cout << "nie ma drogi";
            break;
        }
    }
    return tab;
}
int main(void) {

    bool znaleziono = false;
    list<pair<array<int, 4>, double>> Lista;
    int CelX, CelY, x, y;
    string nazwap = "x.txt";
    int wym2 = 6;
    int wym1 = 6;
    int rows = wym2 + 1;
    int rows2 = wym2 + 1;
    double** G;
    double** MacierzDrogi;
    G = new double* [rows];
    MacierzDrogi = new double* [rows];
    while (rows--) G[rows] = new double[wym1 + 1];
    while (rows2--) MacierzDrogi[rows2] = new double[wym1 + 1];
    cout << "\n\nNacisnij ENTER aby wczytac tablice o nazwie " << nazwap;
    getchar();
    ifstream plik(nazwap.c_str());
    for (unsigned int i = 1; i < wym2 + 1; i++)
    {
        for (unsigned int j = 1; j < wym1 + 1; j++)
        {
            double temp;
            plik >> temp;
            G[i][j] = temp;
            MacierzDrogi[i][j] = 8;
        }
    }
    plik.close();
    wypisztab(G);
    //wypisztab(MacierzDrogi);
    cout << "\n wprowadz wspolrzedne punktu startowego\n\n";
    cout << "x \n";
    cin >> x;
    cout << "y \n";
    cin >> y;
    cout << x + " " << y;
    G[x][y] = 1;
    cout << "\n wprowadz wspolrzedne punktu docelowego\n\n";
    cout << "x \n";
    cin >> CelX;
    cout << "y \n";
    cin >> CelY;
    G[CelX][CelY] = 4;
    //dodaje start do kolejki
    //array int ( pozycjax,pozycjay,kosztdojscia,kierunek,wartosc euherystyki )
    int start = clock();
    priority_queue<pair<array<int, 4>, double>, vector<pair<array<int, 4>, double>>, myComp > OtwarteWezly;
    OtwarteWezly.push({ {x, y,0,-1}, 0 });
    //pair<array<int, 4>, int> top = OtwarteWezly.top();
    int i = x;
    int j = y;

    while (znaleziono == false)
    {
        list<pair<array<int, 4>, double>> DodaneKolejki;
        pair<array<int, 4>, double> top = OtwarteWezly.top();// pobieram wartosc z listy o najmniejszej heurystyce 
        OtwarteWezly.pop();
        //cout << " POZYCJA  " << top.first[0] << " : " << top.first[1] << "KosztBazowy " << top.first[2] << " kierunek rodzica " << top.first[3] << " herystyka " << top.second << endl;
        DodaneKolejki = poruszanie(G, top.first[0], top.first[1], wym1, wym2, CelX, CelY, x, y, top.first[2], Lista, MacierzDrogi);    /// G= Macierz ; i = pozycja Y ; j = pozycja X ; wym1 & wym2 = wymiary macierzy; CelX && CelY = pozycje celu ; x ,y 
        Lista.push_back(top);
        if (DodaneKolejki.empty() == false)
        {
            for (const auto& it : DodaneKolejki)
            {
                OtwarteWezly.push({ { it.first[0],it.first[1],it.first[2],it.first[3]}, it.second });
                if (it.first[0] == CelX && it.first[1] == CelY)
                {
                    znaleziono = true;
                    /wypiszliste(Lista);
                    cout << Lista.size();
                    cout << "droga bez obróbki" << endl;
                    wypisztab(G);
                    cout << "macierz kierunków" << endl;
                    wypisztab(MacierzDrogi);
                    cout << endl;
                    G = znajdzdroge(G, MacierzDrogi, wym1, wym2, x, y, CelX, CelY);
                    for (unsigned int i = 1; i < wym2 + 1; i++)
                    {
                        for (unsigned int j = 1; j < wym1 + 1; j++)
                        {
                            if (G[i][j] == 2)
                            {
                                G[i][j] = 0;
                            }
                        }
                    }
                    G[x][y] = 3;
                    wypisztab(G);
                    cout << endl;
                    ofstream outfile("test.txt");
                    for (unsigned int i = 1; i < wym2 + 1; i++)
                    {
                        for (unsigned int j = 1; j < wym1 + 1; j++)
                        {
                            outfile << G[i][j] << " ";
                        }
                        outfile << endl;
                    }
                }
            }
        }
        DodaneKolejki.clear();
        if (OtwarteWezly.empty())
        {
            cout << "brak osiagalnej sciezki" << endl;
            break;
        }
    }
    for (int i = 0; i < wym2 + 1; i++)
    {
        delete[] G[i];
    }
    //wypisztab(G);
    delete[] G;
    //string nazwap = "x.txt";

    int end = clock();
    std::cout << "it took " << end - start << "ticks, or " << ((float)end - start) / CLOCKS_PER_SEC << "seconds." << std::endl;
    return 0;
}