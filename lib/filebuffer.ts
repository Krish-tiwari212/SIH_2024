import FormData from 'form-data';

export async function createFormDataFromFiles(files: FileList): Promise<FormData> {
    const formdata = new FormData();

    for (let i = 0; i < files.length; i++) {
        let fileBuffer = Buffer.from(await (files[i] as File).arrayBuffer());
        formdata.append('fileInput', fileBuffer, {
            filename: (files[i] as File).name,
            contentType: (files[i] as File).type,
            knownLength: (files[i] as File).size
        });
    }

    return formdata;
}