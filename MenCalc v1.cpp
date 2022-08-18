#include <iostream>
#include <stdlib.h>
using namespace std;

int volume();
int surfaceArea();

class cylinder
{
    public:
    
    float pi=3.141592653;
    float radius,height,sat,volu;
    void tsa()
    {
        cout<<"\nEnter the radius of the cylinder (in m) : ";
        cin>>radius;
        cout<<"\nEnter the height of the cylinder (in m) : ";
        cin>>height;
        sat=2*pi*radius*height;
        cout<<"\nThe Surface area of the given cylinder = "<<sat;
    }
    void vol()
    {
        cout<<"\nEnter the radius of the cylinder (in m) : ";
        cin>>radius;
        cout<<"\nEnter the height of the cylinder (in m) : ";
        cin>>height;
        volu=pi*radius*radius*height*(2/3);
        cout<<"\nThe Volume of the given cylinder = "<<volu;
    }
}c1;
class sphere
{
    public:
    
    float pi=3.141592653;
    float radius,sa,volu;
    void vol()
    {
        cout<<"\nEnter the radius of the sphere (in m) : ";
        cin>>radius;
        volu=(4/3)*pi*radius*radius*radius;
        cout<<"\nThe Volume of the given sphere = "<<volu;
    }
    void tsa()
    {
        cout<<"\nEnter the radius of the sphere (in m) : ";
        cin>>radius;
    }
}sp1;
class cube
{
    public:
    
    float length,sa,volu;
    void tsa()
    {
        cout<<"\nEnter the length of the cube (in m) : ";
        cin>>length;
        sa=6*(length*length);
        cout<<"\nThe Surface area of the given cube = "<<sa;
    }
    void vol()
    {
        cout<<"\nEnter the length of the cube (in m) : ";
        cin>>length;
        volu=length*length*length;
        cout<<"\nThe Volume of the given cube = "<<volu;
    }
}cu1;
class cuboid
{
    public:
    
    float length,breath,hieght,sa,volu;
    void tsa()
    {
        cout<<"\nEnter the length of the cuboid (in m) : ";
        cin>>length;
        cout<<"\nEnter the breath of the cuboid (in m) : ";
        cin>>breath;
        cout<<"\nEnter the hieght of the cuboid (in m) : ";
        cin>>hieght;
        sa=2*length*breath+2*breath*hieght+2*length*hieght;
        cout<<"\nThe Surface area of the given cuboid = "<<sa;
    }
    void vol()
    {
        cout<<"\nEnter the length of the cuboid (in m) : ";
        cin>>length;
        cout<<"\nEnter the breath of the cuboid (in m) : ";
        cin>>breath;
        cout<<"\nEnter the hieght of the cuboid (in m) : ";
        cin>>hieght;
        volu=length*breath*hieght;
        cout<<"\nThe Volume of the given cuboid = "<<volu;
    }
}cub1;
class cone
{
    public:
    
    void vol(){}
    void tsa()
    {}
}con1;
int main() 
{
    int ch=0;
    do
    {
        printf("\n----------------------------------------\n\n\tMENU\n1.Surface Area\n2.Volume\n3.Exit\n\nEnter Your choice (1/2/3) : ");
        cin>>ch;
        printf("\n----------------------------------------\n");
        switch(ch)
        {
            case 1:
                surfaceArea();
                break;
            case 2:
                volume();
                break;
            case 3:
                break;
            default:
                cout<<"\nInvalid choice !!";
                break;
        }
    }while(ch!=3);
    return 0;
}

int volume ()
{
    int ch;
 
    do
    {
        cout<<"\n----------------------------------------\n\n\tMENU=>Volume\n1.Cube\n2.Cuboid\n3.Cylinder\n4.Sphere\n5.Cone\n6.Back to Menu\n\nEnter your choice (1-6) : ";
        cin>>ch;
        printf("\n----------------------------------------\n");
        switch(ch)
        {
            case 1:
                cu1.vol();
                break;
            case 2:
                cub1.vol();
                break;
            case 3:
                c1.vol();
                break;
            case 4:
                sp1.vol();
                break;
            case 5:
                con1.vol();
                break;
            case 6:
                break;
            default :
                cout<<"Invalid choice!!";
                ch=0;
                break;
        }
    }while(ch>6||ch<1);
    return 0;
}

int surfaceArea ()
{
    int ch;
    
    do
    {
        cout<<"\n----------------------------------------\n\n\tMENU=>Surface Area\n1.Cube\n2.Cuboid\n3.Cylinder\n4.Sphere\n5.Cone\n6.Back to Menu\n\nEnter your choice (1-6) : ";
        cin>>ch;
        printf("\n----------------------------------------\n");
        switch(ch)
        {
            case 1:
                cu1.tsa();
                break;
            case 2:
                cub1.tsa();
                break;
            case 3:
                c1.tsa();
                break;
            case 4:
                sp1.tsa();
                break;
            case 5:
                con1.tsa();
                break;
            case 6:
                break;
            default :
                cout<<"Invalid choice!!";
                ch=0;
                break;
        }
    }while(ch>6||ch<1);
    return 0;
}