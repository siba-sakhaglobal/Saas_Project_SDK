import { HttpClient } from '../client';
import type {
  MediaFile,
  PresignUploadResponse,
  PresignDownloadResponse,
  PresignUploadBody,
  RegisterMediaBody,
  PresignDownloadBody,
  BulkDeleteMediaBody,
  MediaListParams,
  MediaStats,
} from '../types/media';
import type { PaginationMetadata } from '../types/common';

export class MediaModule {
  constructor(private client: HttpClient) {}

  /**
   * List media files with pagination and filters
   */
  async listFiles(params?: MediaListParams): Promise<{
    files: MediaFile[];
    pagination: PaginationMetadata;
  }> {
    const response = await this.client.get<{
      files: MediaFile[];
      pagination: PaginationMetadata;
    }>('/api/media', { params });
    return response;
  }

  /**
   * Get a single media file by ID
   */
  async getFile(id: string): Promise<MediaFile> {
    return this.client.get<MediaFile>(`/media/${id}`);
  }

  /**
   * Delete a media file
   */
  async deleteFile(id: string): Promise<void> {
    await this.client.delete(`/media/${id}`);
  }

  /**
   * Get presigned URL for S3 upload
   */
  async presignUpload(body: PresignUploadBody): Promise<PresignUploadResponse> {
    return this.client.post<PresignUploadResponse>('/api/media/presign-upload', body);
  }

  /**
   * Register uploaded file in database
   */
  async registerFile(body: RegisterMediaBody): Promise<MediaFile> {
    return this.client.post<MediaFile>('/api/media/register', body);
  }

  /**
   * Get presigned URL for S3 download
   */
  async presignDownload(body: PresignDownloadBody): Promise<PresignDownloadResponse> {
    return this.client.post<PresignDownloadResponse>('/api/media/presign-download', body);
  }

  /**
   * Bulk delete media files
   */
  async bulkDelete(body: BulkDeleteMediaBody): Promise<void> {
    await this.client.post('/api/media/bulk-delete', body);
  }

  /**
   * Get media statistics
   */
  async getStats(): Promise<MediaStats> {
    return this.client.get<MediaStats>('/api/media/stats');
  }
}
