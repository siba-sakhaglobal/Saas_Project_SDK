import { DateTime, UUID } from './common';

/**
 * Media file response object
 */
export interface MediaFile {
  id: UUID;
  fileName: string;
  fileType: 'image' | 'video' | 'audio' | 'document' | 'other';
  mimeType: string;
  sizeBytes: number;
  s3Key: string;
  url: string;
  formattedSize: string;
  createdAt: DateTime;
  updatedAt: DateTime;
}

/**
 * Presign upload response (for S3 direct upload)
 */
export interface PresignUploadResponse {
  uploadUrl: string;
  key: string;
  expiresAt: DateTime;
}

/**
 * Presign download response (for S3 direct download)
 */
export interface PresignDownloadResponse {
  downloadUrl: string;
  expiresAt: DateTime;
}

/**
 * Presign upload request body
 */
export interface PresignUploadBody {
  filename: string;
  contentType?: string;
  expiresInSec?: number;
}

/**
 * Register uploaded file request body
 */
export interface RegisterMediaBody {
  fileName: string;
  fileType: string;
  mimeType: string;
  sizeBytes: number;
  s3Key: string;
  url: string;
}

/**
 * Presign download request body
 */
export interface PresignDownloadBody {
  key: string;
  expiresInSec?: number;
}

/**
 * Bulk delete request body
 */
export interface BulkDeleteMediaBody {
  ids: UUID[];
}

/**
 * Media list query parameters
 */
export interface MediaListParams {
  page?: number;
  limit?: number;
  type?: 'image' | 'video' | 'audio' | 'document' | 'other' | 'all';
  search?: string;
  category?: 'blog' | 'events' | 'team' | 'products' | 'donations' | 'assets' | 'all';
}

/**
 * Media statistics response
 */
export interface MediaStats {
  total: number;
  images: number;
  videos: number;
  audio: number;
  documents: number;
  other: number;
  totalSizeBytes: number;
}
