from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from apps.home.models import FakturPembelian, JenisProduk, Produk, DetailProduk, DetailFakturPembelian
from .serializers import ItemSerializerPembelian, ItemSerializerJenisProduk
from datetime import datetime
from apps.home.views import update_harga_jual_to_database


@api_view(['GET'])
def no_faktur(request):
    no_faktur_pembelian = FakturPembelian.objects.values('no_faktur_pembelian')
    serializer = ItemSerializerPembelian(no_faktur_pembelian, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def jenis_produk(request):
    jenis_produk = JenisProduk.objects.values('nama_jenis_produk')
    serializer = ItemSerializerJenisProduk(jenis_produk, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def auth(request):
    data = request.data

    username = data.get("username")
    password = data.get("password")

    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_superuser:
            return Response({'message': 'Success'})
        return Response({'message': 'Akun anda tidak memiliki otoritas di aplikasi ini'})
    return Response({'message': 'Username password salah!'})


@api_view(['POST'])
def addProduk(request):
    data = request.data
    """
    sample_body = {
        "nama_produk": "Jordan 1 Kg",
        "jenis_produk": "herbisida",
        "no_faktur_pembelian": "42",
        "kuantitas": "9",
        "harga_satuan": "20000.0",
        "tanggal_kadaluarsa": "24 Nov 2022"
    }
    """

    add_produk = Produk.objects. \
        create(nama_produk=data.get('nama_produk'),
               jenis_produk=JenisProduk.objects.get(nama_jenis_produk=data.get('jenis_produk')))

    DetailFakturPembelian.objects.create(
        faktur_pembelian=FakturPembelian.objects.get(
            no_faktur_pembelian=data.get('no_faktur_pembelian')),
        produk=Produk.objects.get(id_produk=add_produk.id_produk),
        kuantitas=data.get('kuantitas'),
        harga_satuan=data.get('harga_satuan')
    )

    DetailProduk.objects.create(
        faktur_pembelian=FakturPembelian.objects.get(
            no_faktur_pembelian=data.get('no_faktur_pembelian')),
        produk=Produk.objects.get(id_produk=add_produk.id_produk),
        stok=data.get('kuantitas'),
        tanggal_kadaluarsa=datetime.strptime(data.get('tanggal_kadaluarsa'), '%d %b %Y'),
        harga_jual_satuan=float(data.get('harga_satuan')) * 0.2 + float(
            data.get('harga_satuan'))
    )

    update_harga_jual_to_database(data.get('nama_produk'), data.get('jenis_produk'))
    return Response(data)
