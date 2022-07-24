from django.core.files.uploadedfile import SimpleUploadedFile

mockedUploadedFrogImage = SimpleUploadedFile(
                                name='test_image.png',
                                content=open(
                                    '/app/core/tests/test_image.png', 'rb')
                                .read(),
                                content_type='image/jpeg'
                            )
